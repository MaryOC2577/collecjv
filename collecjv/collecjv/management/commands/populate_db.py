import requests
from django.core.management.base import BaseCommand
from collecjv.models import Game, Company


class Command(BaseCommand):
    # def company_name(self, id):

    #     # stream = requests.post('https://api.igdb.com/v4/companies', headers=headers, data="fields name; where id={id};")
    #     pass

    # def area_name(self, name):

    #     # stream = requests.post('https://api.igdb.com/v4/regions', headers=headers, data="fields name; where id={id};")
    #     pass

    def handle(self, *args, **options):
        client_id = "mn03z6fvnt221t7uo6gby9ltfhwbqq"
        client_secret = "4y3rm04ml420jc1b2mijzvcun4cscx"

        body = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        }
        r = requests.post("https://id.twitch.tv/oauth2/token", body)

        # data output
        keys = r.json()

        print(keys)

        headers = {
            "Client-ID": client_id,
            "Authorization": "Bearer " + keys["access_token"],
        }

        print(headers)

        stream = requests.post(
            "https://api.igdb.com/v4/games",
            headers=headers,
            data="fields id, name, involved_companies,summary, game_localizations, platforms.name; limit 500;",
        )

        game_data = stream.json()

        for game in game_data:
            print(game)
            if game.get("involved_companies","") and game.get("game_localizations",""):
                cpy = Company.objects.get_or_create(
                    name=game.get("involved_companies", ""), area=game.get("game_localizations")
                )
                one_game = Game.objects.get_or_create(
                    name=game.get("name"),
                    description=game.get("summary"),
                    category="",
                    platform=None,
                )
                print(one_game)
                one_game[0].company.add(cpy[0])
                one_game[0].save()
