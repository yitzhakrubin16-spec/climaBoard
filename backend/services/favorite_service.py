from schemas.favorites import FavoriteCreate

favorites = []

def add_favorite_service(favorite: FavoriteCreate):
    favorites.append(favorite)
    return favorite