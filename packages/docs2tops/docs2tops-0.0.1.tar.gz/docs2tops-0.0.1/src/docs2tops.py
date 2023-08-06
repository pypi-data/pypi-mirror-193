from utils.functions import *


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