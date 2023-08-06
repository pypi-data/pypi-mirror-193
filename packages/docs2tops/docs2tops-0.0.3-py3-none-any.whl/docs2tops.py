# all in one


import pandas as pd
import numpy as np
import nltk
from nltk.corpus import words as global_words
import re
from tqdm import tqdm
from random import sample
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from keyphrase_vectorizers import KeyphraseCountVectorizer
from keybert import KeyBERT
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

nltk.download('words')
nltk.download('stopwords')
global_vocab = global_words.words()



def basic_clean(text, apply_stopwords=True, apply_lemmatizer=False):
    """
    A simple function to clean up the data. All the words that
    are not designated as a stop word is then lemmatized after
    encoding and basic regex parsing are performed.
    """
    wnl = nltk.stem.WordNetLemmatizer()
    stopwords = nltk.corpus.stopwords.words('english')
    if apply_stopwords == False:
        stopwords = ['']
    # add space before punctuations
    pattern = r"""[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"""
    text = re.sub(pattern, r' \g<0>', text)

    words = re.sub(r'[^\w\s]', '', text).split()
    if apply_lemmatizer == True:
        return [wnl.lemmatize(word).lower() for word in words if word not in stopwords]
    else:
        return [word.lower() for word in words if word not in stopwords]


def extract_ngram(corpus):
    corpus_words = basic_clean(''.join(str(corpus)))

    ngrams1_series = (pd.Series(nltk.ngrams(corpus_words, 1)))
    ngrams1_series_list = []
    for ngram in ngrams1_series:
        it = str(' '.join(ngram))
        ngrams1_series_list.append(it)
    ngrams1_series_list = list(set(ngrams1_series_list))
    print('length of unique 1 grams: ', len(ngrams1_series_list))

    ####
    # with st.spinner('Extracting N-grams and filtering by their relativeness and usefullness'):
    meaningful_1_grams = []
    meaningless_1_grams = []
    alphabetical_words = []
    word_not_in_vocabulary = []
    print('Extracting ngrams')
    for word in tqdm(ngrams1_series_list):
        word = word.lower()
        if word.isalpha():
            if word in global_vocab:
                meaningful_1_grams.append(word)
                alphabetical_words.append(word)
            else:
                word_not_in_vocabulary.append(word)
                if len(word) < 25:
                    alphabetical_words.append(word)

        elif word[0] != 'x' and not word.isnumeric():
            meaningful_1_grams.append(word)
            alphabetical_words.append(word)
        else:
            meaningless_1_grams.append(word)

    non_numeric_words = meaningful_1_grams + word_not_in_vocabulary
    non_numeric_words_1grams = list(set(non_numeric_words))
    return meaningful_1_grams, meaningless_1_grams, alphabetical_words

def divide_data_to_chunks(data: list, chunksize=32):
    list_of_lists = []
    for i in range(0, len(data), chunksize):
        chunk = data[i:i + chunksize]
        list_of_lists.append(chunk)
    return list_of_lists


def keyword_extraction(docs_chunks):
    print('Extracting moregrams')
    kw_model = KeyBERT()
    all_output_from_keybert = []

    for chunk in tqdm(docs_chunks):
        keybert_res = kw_model.extract_keywords(docs=chunk, vectorizer=KeyphraseCountVectorizer(),
                                                nr_candidates=20, top_n=15, use_mmr=True,
                                                diversity=0.4, stop_words='english')
        all_output_from_keybert.extend(keybert_res)
    return all_output_from_keybert


def create_dictionary_with_user_defined_topics(inputted_candidate_labels, embedder, corpus_embeddings, keywords):
    candidate_labels = inputted_candidate_labels  # ["price", "age", "delivery late", "time", 'color', 'positive', 'ingredients natural', 'meat type']
    candidate_embeddings = embedder.encode(candidate_labels, convert_to_tensor=True)
    candidate_embeddings = candidate_embeddings / np.linalg.norm(candidate_embeddings, axis=1, keepdims=True)

    cosim_matrix = cosine_similarity(corpus_embeddings, candidate_embeddings)
    matrix_df = pd.DataFrame(cosim_matrix)
    matrix_df.columns = candidate_labels
    matrix_df['max'] = matrix_df.max(axis=1)

    colname_of_maxs = []
    for row_id in range(matrix_df.shape[0]):
        max_score = float(matrix_df.iloc[row_id, -1])
        list_of_scores = list(matrix_df.iloc[row_id, :-1])
        index_of_max = list_of_scores.index(max_score)
        colname_of_max = matrix_df.columns[index_of_max]
        colname_of_maxs.append(colname_of_max)

    matrix_df['max_colname'] = colname_of_maxs
    matrix_df.index = keywords
    return matrix_df


def built_dict(matrix_df, threshold=0.55, output_as_dict=False):
    df = matrix_df[matrix_df['max'] > threshold]
    df = df.reset_index()
    df = df[['index', 'max_colname']]
    df.columns = ['keyword', 'topic']

    df_dict = pd.DataFrame()
    for topic_ in df.topic.value_counts().index.tolist():  # or descending order
        keywords_ = list(df[df['topic'] == topic_]['keyword'])
        df_dict[topic_] = keywords_ + [''] * (df_dict.shape[0] - len(keywords_))
    if not output_as_dict:
        return df_dict
    else:
        df_dict_dict = {}
        for col in df_dict:
            unique_values = list(set(df_dict[col]))
            unique_values = [x for x in unique_values if x]
            df_dict_dict[col] = unique_values
        return df_dict_dict


def extract_keywords_with_keybert(docs, chunksize, sample_size=1000):
    docs = sample(docs, min(len(docs), sample_size))
    print('Sample size for moregrams:', sample_size)
    docs_chunks = divide_data_to_chunks(docs, chunksize=chunksize)

    all_output_from_keybert = keyword_extraction(docs_chunks=docs_chunks)

    keywords = []
    for element in all_output_from_keybert:
        for el in element:
            keyword = el[0]
            keywords.append(keyword)
    keywords = list(set(keywords))
    return keywords


def take_only_strings_from_docs(docs):

    print('original number of docs: ', len(docs))
    docs = list(set(docs))
    only_string_docs = []

    for doc in docs:
        if isinstance(doc, str):
            only_string_docs.append(doc)

    docs = only_string_docs
    print('unique number of docs: ', len(docs))
    return docs

def load_models():
    print('Embedding model is loading')
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    print('Embedding model is loaded')
    print('Auto labeling model is loading')
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    print('Auto labeling model is loaded')
    return embedder, model, tokenizer

def create_basic_keywords(docs):
    meaningful_1_grams, meaningless_1_grams, alphabetical_words = extract_ngram(corpus=docs)
    basic_keywords = meaningful_1_grams + alphabetical_words
    return basic_keywords


# def select_sample_size_for_keybert(sample_size=min(len(docs_input_list), 1000)):
#     return sample_size
#
# # selected_sample_size = select_sample_size_for_keybert()
#
# def select_candidate_labels(list_of_words=None):
#     if list_of_words is None:
#         list_of_words = candidate_topics_list_default
#     return list_of_words

# for keybert
# selected_sample_size = min(len(docs), selected_sample_size)
# docs = sample(docs, selected_sample_size)
# print('sample size -  number of docs: ', len(docs))


###############
############ Auto dictionary functions
#####################

def cluster2py_dictionary(clusters, keywords):
    # cluster dictionary
    cluster_dict = {}
    for cluster_id, cluster in enumerate(clusters):
        members = []
        for sentence_id in cluster:
            members.append(keywords[sentence_id])
        cluster_dict[cluster_id] = members
    return cluster_dict


def cluster2py_df(clusters, keywords):
    # create cluster dataframe
    cluster_ids = []
    keywords_ = []

    for cluster_id, cluster in enumerate(clusters):
        for element_id in cluster:
            keywords_.append(keywords[element_id])
            cluster_ids.append(cluster_id)

    cluster_df = pd.DataFrame()

    cluster_df['keyword'] = keywords_
    cluster_df['cluster_id'] = cluster_ids
    return cluster_df

def cluster_labeling(tokenizer, model, cluster_dict):
    print('Labeling clusters (auto-topics)')
    labels = []
    for cluster_id in tqdm(range(0, len(cluster_dict))):
        # prompt = f"""What is the topic of the words in one word?.
        prompt = f"""What word can summarize the words below: {sample(cluster_dict[cluster_id], min(15, len(cluster_dict[cluster_id])))}"""

        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs)
        res = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        labels.append(res[0].split(',')[0])
    return labels

def map_names_to_cluster_df(cluster_df, labels):
    mapping_dict = {}
    for idx, cluster_id in enumerate(cluster_df['cluster_id'].unique()):
        mapping_dict[cluster_id] = labels[idx]
    cluster_df['cluster_label'] = cluster_df['cluster_id'].map(mapping_dict)
    return cluster_df

def built_dict_auto(cluster_df):
    cluster_df2 = cluster_df[['keyword', 'cluster_label']]
    df_dict2 = pd.DataFrame()
    for topic_ in cluster_df2.cluster_label.value_counts().index.tolist():  # or descending order
        keywords2_ = list(cluster_df2[cluster_df2['cluster_label'] == topic_]['keyword'])
        df_dict2[topic_] = keywords2_ + [''] * (df_dict2.shape[0] - len(keywords2_))
    return df_dict2

def check_auto_dictionary(auto_dict):
    ratios = []
    global_vocab = global_words.words()

    for col_id in tqdm(range(auto_dict.shape[1])):
        keywords_in_auto_dict = auto_dict.iloc[:, col_id].values
        only_alpha_words = []
        alpha_words_count = 0

        for words in keywords_in_auto_dict:
            words = words.split()
            for word in words:
                if word.isalpha():
                    alpha_words_count += 1
                    only_alpha_words.append(word)
            non_alpha_words_count = len(keywords_in_auto_dict) - alpha_words_count

        valid_words = []
        invalid_words = []
        for words in keywords_in_auto_dict:
            words = words.split()
            for word in words:
                if word in global_vocab:
                    valid_words.append(word)
                else:
                    invalid_words.append(word)
        if len(only_alpha_words) == 0:
            only_alpha_words = ['']
        ratio = round(len(valid_words) / len(only_alpha_words), 2)
        ratios.append(ratio)
    return ratios


def matrix_colnames(col_labels, col_embeddings):
    cosim_matrix = cosine_similarity(col_embeddings, col_embeddings)
    matrix_df = pd.DataFrame(cosim_matrix)
    matrix_df.columns = col_labels

    # df = df.replace(['old value'], 'new value')
    #  matrix_df['max'] = matrix_df.max(axis=1)
    maxs = []
    for row in range(matrix_df.shape[0]):
        max_ = sorted(set(matrix_df.iloc[row, :]))[-2]
        maxs.append(max_)
    matrix_df['max'] = maxs

    colname_of_maxs = []
    for row_id in range(matrix_df.shape[0]):
        max_score = maxs[row_id]
        list_of_scores = list(matrix_df.iloc[row_id, :-1])
        index_of_max = list_of_scores.index(max_score)
        colname_of_max = matrix_df.columns[index_of_max]
        colname_of_maxs.append(colname_of_max)

    matrix_df['max_colname'] = colname_of_maxs

    matrix_df.index = col_labels
    return matrix_df


def merging_similar_clusters(auto_dict, embedder, similar_column_tresh=0.65):
    col_labels = auto_dict.columns.tolist()
    col_embeddings = embedder.encode(col_labels, convert_to_tensor=True)
    col_embeddings = col_embeddings / np.linalg.norm(col_embeddings, axis=1, keepdims=True)
    res_label_matrix = matrix_colnames(col_labels=col_labels, col_embeddings=col_embeddings)

    main_columns = list(res_label_matrix[res_label_matrix['max'] > similar_column_tresh]['max_colname'].index)
    similar_colnames = list(res_label_matrix[res_label_matrix['max'] > similar_column_tresh]['max_colname'])
    new_auto_dict = pd.DataFrame({'index_column': list(range(1, 1001))})

    for idx in range(len(main_columns)):
        if similar_colnames[idx] not in new_auto_dict.columns:
            joind_values = list(set(auto_dict[main_columns[idx]])) + list(set(auto_dict[similar_colnames[idx]]))
            joind_values = [x for x in joind_values if x]
            new_auto_dict[main_columns[idx]] = joind_values + [''] * (1000 - len(joind_values))

    rest_dict_df = auto_dict.drop(main_columns + similar_colnames, axis=1)

    for col in rest_dict_df.columns:
        new_auto_dict[col] = rest_dict_df[col]

    new_auto_dict = new_auto_dict.replace('', np.nan)
    return new_auto_dict

def final_touches(new_auto_dict, lemmatize_dict_outputs=False, output_as_dict=False):
    new_auto_dict = new_auto_dict.drop(columns=['index_column'])
    for row in range(new_auto_dict.shape[0]):
        if len(set(new_auto_dict.iloc[row, :])) < 2:
            max_row_length = row
            # print(max_row_length)
            break

    new_auto_dict = new_auto_dict.iloc[:max_row_length, :]

    if lemmatize_dict_outputs:
        wnl = nltk.stem.WordNetLemmatizer()

        for col in new_auto_dict:
            colvalues = new_auto_dict[col].tolist()
            new_elements = []
            for element in colvalues:
                if isinstance(element, str):
                    new_element = wnl.lemmatize(element).lower()
                else:
                    new_element = ''
                    for subelement in element:
                        new_subelement = wnl.lemmatize(subelement).lower()
                        new_element += new_subelement
                new_elements.append(new_element)
            new_auto_dict[col] = new_elements

    for col in new_auto_dict:
        unique_values = list(set(new_auto_dict[col]))
        unique_values = [x for x in unique_values if x]
        unique_values = [x for x in unique_values if str(x) != 'nan']
        new_auto_dict[col] = unique_values + (new_auto_dict.shape[0] - len(unique_values)) * ['']


    if not output_as_dict:
        return new_auto_dict

    if output_as_dict:
        new_auto_dict_dict = {}
        for col in new_auto_dict:
            unique_values = list(set(new_auto_dict[col]))
            unique_values = [x for x in unique_values if x]
            new_auto_dict_dict[col] = unique_values
        return new_auto_dict_dict





def auto_dictionary_main(corpus_embeddings, keywords, tokenizer, model, embedder, output_as_dict):
    clusters = util.community_detection(corpus_embeddings, min_community_size=10, threshold=0.65)

    cluster_dict = cluster2py_dictionary(clusters=clusters, keywords=keywords)
    cluster_df = cluster2py_df(clusters=clusters, keywords=keywords)

    # create dictionary topic names
    labels = cluster_labeling(tokenizer=tokenizer, model=model, cluster_dict=cluster_dict)

    # add those names to dictionary dataframe
    cluster_df = map_names_to_cluster_df(cluster_df=cluster_df, labels=labels)

    # build first dictionary
    auto_dict = built_dict_auto(cluster_df=cluster_df)

    print('Checking auto-created dictionary and correcting')
    ratios = check_auto_dictionary(auto_dict=auto_dict)
    ratio_df = pd.DataFrame({'ratios': ratios, 'colname': auto_dict.columns})

    ## valid words ratio in alphabetical keywords of each column
    id_list_of_meaningless_columns = list(ratio_df[ratio_df['ratios'] < 0.4].index)
    auto_dict = auto_dict.drop(auto_dict.columns[id_list_of_meaningless_columns], axis=1)

    print('Merging similar topics')
    # find similar columns (topics/clusters) by only their names and merge them
    new_auto_dict = merging_similar_clusters(auto_dict=auto_dict, embedder=embedder, similar_column_tresh=0.65)

    # final touches
    new_auto_dict = final_touches(new_auto_dict=new_auto_dict, output_as_dict=output_as_dict, lemmatize_dict_outputs=False)
    return new_auto_dict




def docs2tops(candidate_topics_list=None, docs_input_list=None, moregrams_sample_size=None, output_as_dict=True):
    embedder, model, tokenizer = load_models()

    # adjusting names for functions
    docs = docs_input_list
    docs = take_only_strings_from_docs(docs=docs)
    basic_keywords = create_basic_keywords(docs=docs)

    # extract moregrams with keybert
    if moregrams_sample_size is not None:
        keywords = extract_keywords_with_keybert(docs=docs, chunksize=100, sample_size=moregrams_sample_size)
        # joining keybert keywords with 1-grams
        keywords = basic_keywords + keywords
        keywords = list(set(keywords))
    else:
        keywords = basic_keywords

    # embed the keywords
    print('Embedding started')
    corpus_embeddings = embedder.encode(keywords, batch_size=124, show_progress_bar=True, convert_to_tensor=True)
    corpus_embeddings = corpus_embeddings / np.linalg.norm(corpus_embeddings, axis=1, keepdims=True)

    df_dict_with_user_input = False
    if candidate_topics_list:
        inputted_candidate_labels = candidate_topics_list
        print('Creating dictionary with user-inputs')
        matrix_df = create_dictionary_with_user_defined_topics(inputted_candidate_labels=inputted_candidate_labels,
                                                               embedder=embedder,
                                                               corpus_embeddings=corpus_embeddings,
                                                               keywords=keywords)

        dict_with_user_input = built_dict(matrix_df=matrix_df, threshold=0.55, output_as_dict=output_as_dict)


    print('Auto dictionary is being created...')
    new_auto_dict = auto_dictionary_main(corpus_embeddings=corpus_embeddings,
                                         keywords=keywords,
                                         tokenizer=tokenizer,
                                         model=model,
                                         embedder=embedder,
                                         output_as_dict=output_as_dict)

    try:
        return dict_with_user_input, new_auto_dict
    except:
        dict_with_user_input = {'N/A': 'no pre-topics provided by user'}
        return dict_with_user_input, new_auto_dict
