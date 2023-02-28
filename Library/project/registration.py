from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"

        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"

        library.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str, library: Library):
        try:
            user_found = next(filter(lambda x: x.user_id == user_id, library.user_records))
            old_username = user_found.username
            if user_found.username != new_username:
                user_found.username = new_username
                if old_username in library.rented_books:
                    contents = library.rented_books[old_username]
                    library.rented_books[new_username] = contents
                    del library.rented_books[old_username]

                return f"Username successfully changed to: {new_username} for user id: {user_id}"
            else:
                return f"Please check again the provided username - it should be different than the username used so far!"

        except StopIteration:
            return f"There is no user with id = {user_id}!"
