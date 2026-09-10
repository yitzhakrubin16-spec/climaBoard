from schemas.favorites import FavoriteCreate

favorites = []

def add_favorite_service(favorite: FavoriteCreate):
    favorites.append(favorite)
    return favorite

def get_favorites_service(user_name: str):
    user_favorites = []

    for favorite in favorites:
        if favorite.user_name == user_name:
            user_favorites.append(favorite)

    return user_favorites        

def delete_favorite_service(user_name: str, city_id: int):

    for i in range(len(favorites)):
        if favorites[i].user_name == user_name and favorites[i].city_id == city_id:
            return favorites.pop(i)

    return None                 
