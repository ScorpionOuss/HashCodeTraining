#!/usr/bin/env python3
from readData import streaming_data
from evaluate import evaluate

print(streaming_data.V, streaming_data.C, streaming_data.X)


def compute_videos_ranking():
    """
        
        """
    videos_ranking = [0 for _ in range(streaming_data.V)]

    for request in streaming_data.Requests:
        videos_ranking[request.idVideo] += request.numReq

    return videos_ranking


def suboptimal_video_placement():
    """
    Find the optimal video placement
    """

    # Compute the ranking of the different videos in regards to the number of requests
    videos_scores = compute_videos_ranking()

    videos_ranking = sorted([(videos_scores[i], i) for i in range(len(videos_scores))], reverse=True)

    used_caches = 0
    currentVideo = 0


def optimal_video_placement():
    # Compute the score of videos in regrads to requests
    videos_scores = compute_videos_ranking()
    # Sort the videos
    videos_ranking = sorted([(videos_scores[i], i) for i in range(len(videos_scores))], reverse=True)

    cache_distribution = [[0, []] for _ in range(streaming_data.C)]

    for video in videos_ranking:
        size = streaming_data.Sizes[video[1]]
        for cache in cache_distribution:
            print(size, streaming_data.X - cache[0])
            if size < streaming_data.X - cache[0]:
                cache[0] += size
                cache[1].append(video[1])
                break

    return {i: cache_distribution[i][1] for i in range(streaming_data.C)}


op_placements = optimal_video_placement()

print(op_placements)
print(evaluate(op_placements))
