def solution(genres, plays):

    genre_play_count_dict = dict()
    plays_in_genre = dict()

    for num, genre in enumerate(genres):
        if genre_play_count_dict.get(genre, 0) == 0:
            genre_play_count_dict[genre] = plays[num]
            plays_in_genre[genre]= [[num, plays[num]]]
        else:
            genre_play_count_dict[genre] += plays[num]
            plays_in_genre[genre].append([num,plays[num]])

    genre_play_count = [[key,value] for key,value in genre_play_count_dict.items()]
    genre_play_count = sorted(genre_play_count, key= lambda x : x[1], reverse=True)

    answer = []
    for genre in genre_play_count:
        _list = plays_in_genre[genre[0]]
        _list = sorted(_list, key = lambda x : x[1], reverse=True)
        answer += [x[0] for x in _list][0:2]

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))