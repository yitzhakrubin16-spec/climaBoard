from schemas.favorites import FavoriteCreate

favorites = []

def add_favorite_service(favorite: FavoriteCreate):
    favorites.append(favorite)
    return favorite

def get_favorites_service(user_name: str):
    user_favorites = []

    for i in range(len(favorites)):
        if favorites[i].user_name == user_name:
            user_favorites.append(favorites[i])

    return user_favorites        