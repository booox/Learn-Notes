VIDEOS = {'Animals': [{'name': 'Crab',
                       'thumb': 'http://www.vidsplay.com/vids/crab.jpg',
                       'video': 'http://www.vidsplay.com/vids/crab.mp4',
                       'genre': 'Animals'},
                      {'name': 'Alligator',
                       'thumb': 'http://www.vidsplay.com/vids/alligator.jpg',
                       'video': 'http://www.vidsplay.com/vids/alligator.mp4',
                       'genre': 'Animals'},
                      {'name': 'Turtle',
                       'thumb': 'http://www.vidsplay.com/vids/turtle.jpg',
                       'video': 'http://www.vidsplay.com/vids/turtle.mp4',
                       'genre': 'Animals'}
                      ],
            'Cars': [{'name': 'Postal Truck',
                      'thumb': 'http://www.vidsplay.com/vids/us_postal.jpg',
                      'video': 'http://www.vidsplay.com/vids/us_postal.mp4',
                      'genre': 'Cars'},
                     {'name': 'Traffic',
                      'thumb': 'http://www.vidsplay.com/vids/traffic1.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic1.avi',
                      'genre': 'Cars'},
                     {'name': 'Traffic Arrows',
                      'thumb': 'http://www.vidsplay.com/vids/traffic_arrows.jpg',
                      'video': 'http://www.vidsplay.com/vids/traffic_arrows.mp4',
                      'genre': 'Cars'}
                     ],
            'Food': [{'name': 'Chicken',
                      'thumb': 'http://www.vidsplay.com/vids/chicken.jpg',
                      'video': 'http://www.vidsplay.com/vids/bbqchicken.mp4',
                      'genre': 'Food'},
                     {'name': 'Hamburger',
                      'thumb': 'http://www.vidsplay.com/vids/hamburger.jpg',
                      'video': 'http://www.vidsplay.com/vids/hamburger.mp4',
                      'genre': 'Food'},
                     {'name': 'Pizza',
                      'thumb': 'http://www.vidsplay.com/vids/pizza.jpg',
                      'video': 'http://www.vidsplay.com/vids/pizza.mp4',
                      'genre': 'Food'}
                     ]}


def get_categories():
    """
    Get the list of video categories.
    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    :return: list
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.
    Here you can insert some parsing code that retrieves
    the list of videostreams in a given category from some site or server.

    :param category: str
    :return: list
    """
    return VIDEOS[category]

cates = get_categories()
# print cates
# print get_videos('Cars')