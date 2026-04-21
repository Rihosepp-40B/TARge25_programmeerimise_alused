if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"