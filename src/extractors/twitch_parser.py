thondef parse_twitch_video_data(data):
    parsed_data = []
    for video in data['videos']:
        video_info = {
            "createdAt": video["created_at"],
            "owner": {
                "id": video["channel"]["_id"],
                "displayName": video["channel"]["display_name"],
                "login": video["channel"]["name"],
            },
            "id": video["_id"],
            "game": {
                "id": video["game"]["_id"],
                "name": video["game"]["name"],
                "slug": video["game"]["slug"]
            },
            "lengthSeconds": video["length"],
            "previewThumbnailURL": video["thumbnail_url"],
            "title": video["title"],
            "viewCount": video["view_count"],
            "keyword": video["keyword"]  # Assuming keyword is returned in API response
        }
        parsed_data.append(video_info)
    return parsed_data