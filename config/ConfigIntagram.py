import instaloader
from model.User import User


class ConfigInstagram:

    def __init__(self):
        self.__username = 'irineu.almeida.jr'
        self.__password = 'colocar_senha'
        self.__bot = instaloader.Instaloader()
        # self.__bot.login(self.__username, self.__password)
        self.__profile = instaloader.Profile

    def load(self):
        users = [User(
            id=1,
            name='Alane',
            instagram_username='alanediax',
            followers=0,
            url_image='https://s2.glbimg.com/1qmlbxsM-qVrrWQk8eLu7YI0GUQ=/i.s3.glbimg.com/v1'
                      '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/T/H/3I6H0BTMqO5tUF8G5mNw'
                      '/cabecograma-330x270-0015-17-alanis.png'
        ),
            User(
                id=2,
                name='Beatriz',
                instagram_username='beatrizreisbrasil',
                followers=0,
                url_image='https://s2.glbimg.com/qloI2ImVBE6zQNTmfz6rr7NubYM=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/0/a/yih0KWQBmo4zf0SOOA1A'
                          '/cabecograma-330x270-0027-33-beatrizl.png'
            ),
            User(
                id=3,
                name='Deniziane',
                instagram_username='anny_ferreira10',
                followers=0,
                url_image='https://s2.glbimg.com/FKuXDmRs6r9l0kp-AM75cn6S7Kc=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/j/i/UQP8bgQCyvdOBPzo98YQ'
                          '/cabecograma-330x270-0030-8-anne.png'
            ),
            User(  ##---- NÃO FUNCIONA
                id=4,
                name='Fernanda',
                instagram_username='nandabande',
                followers=0,
                url_image='https://s2.glbimg.com/M_qF_zCLSDXn5VwJjeYndP0ylVc=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/a/G/3OpFqSRmm2kOeRkcjD5w'
                          '/cabecograma-330x270-0007-10-fernanda.png'
            ),
            User(
                id=5,
                name='Giovanna',
                instagram_username='giovannaleticiamarinho',
                followers=0,
                url_image='hhttps://s2.glbimg.com/bPpKpAk16RUL0Vr7qO8B5uxApls=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/U/q/nLQhAbQfS5dDZakZH3Zg'
                          '/cabecograma-330x270-0028-32-giovanna-pitel.png'
            ),
            User(
                id=6,
                name='Leidy Elin',
                instagram_username='leidyelin',
                followers=0,
                url_image='https://s2.glbimg.com/SjXsFdI2Nuw9Uh40cr7WCNVXtNY=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/1/I/BkC6n7QNW3QdyYVxswbA'
                          '/cabecograma-330x270-0008-1-leidi.png'
            ),
            User(
                id=7,
                name='Lucas Luigi',
                instagram_username='lucas.luigi',
                followers=0,
                url_image='https://s2.glbimg.com/bxMjqvBNUDccgxHsKkn3QqNiKbE=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/L/i/Z3Q2AQSi6VyrElQorYig'
                          '/cabecograma-330x270-0006-11-luigi.png'
            ),
            User(
                id=8,
                name='Lucas Pizane',
                instagram_username='lucaspizane',
                followers=0,
                url_image='https://s2.glbimg.com/2MWtpSdfIitmGLjhiVarVc7lf0k=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/k/H/LezltFSGmwNE1BgQJWZw'
                          '/cabecograma-330x270-0031-7-pizzani.png'
            ),
            User(
                id=9,
                name='Marcus',
                instagram_username='marcus.vib',
                followers=0,
                url_image='https://s2.glbimg.com/jjgu-2EsQBvjABQnLFiegmShuWI=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/w/D/aNSiS7QJAvRb5uKFGzbg'
                          '/cabecograma-330x270-0017-15-marcos.png'
            ),
            User(
                id=10,
                name='Matteus',
                instagram_username='bahmatteus',
                followers=0,
                url_image='https://s2.glbimg.com/FM_iOFbZx7h2jaPNgKAU0ZoKFuk=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/6/p/aBB99gTNGIUs1NW3tuhA'
                          '/cabecograma-330x270-0009-28-matteus.png'
            ),
            User(
                id=11,
                name='Maycon',
                instagram_username='mayconcosmer',
                followers=0,
                url_image='https://s2.glbimg.com/Jf-7vMYMSf-PkoBf7VPPaAXlHGI=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/n/9/y6AZBQQreIam7UA6xkWw'
                          '/cabecograma-330x270-0014-18-maycon.png'
            ),
            User(
                id=12,
                name='Mc Bin Laden',
                instagram_username='mcbinladen',
                followers=0,
                url_image='https://s2.glbimg.com/LjAhPazcpK0E08GxYrcsNTR2arE=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/4/9/v6CZHuTc2QBfBWqPX9Ug'
                          '/cabecograma-330x270-0022-3-jefferson.png'
            ),
            User(
                id=13,
                name='Nizam',
                instagram_username='aboujokh',
                followers=0,
                url_image='https://s2.glbimg.com/RDhoHlG6-Hv9gnTBGFcl2201JUE=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/K/M/dPD3WLQoeVM5AXjhjBHQ'
                          '/cabecograma-330x270-0032-6-nissam.png'
            ),
            User(
                id=14,
                name='Rodriguinho',
                instagram_username='rodriguinho',
                followers=0,
                url_image='https://s2.glbimg.com/milgdMnod_FJyaEHCBQrL36rPKc=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/f/r/Jggwk1SSaFXJAOk0X5AA'
                          '/cabecograma-330x270-0034-4-rodrigo.png'
            ),
            User(
                id=15,
                name='Vanessa Lopes',
                instagram_username='vanessalopesr_',
                followers=0,
                url_image='https://s2.glbimg.com/mVEMnAox73wHySK9Zh-Eu-req5Q=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/U/o/bXTZLSTtixi5r6e4pIYw'
                          '/cabecograma-330x270-0004-14-vanessa.png'
            ),
            User(
                id=16,
                name='Vinicius Rodrigues',
                instagram_username='viniciusbellator.rodrigues',
                followers=0,
                url_image='https://s2.glbimg.com/GwqemLLWNI29hZ6bMwosuYvEQ_0=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/T/y/vSL5KkQAapuCcyHBotTA'
                          '/cabecograma-330x270-0003-13-vinicius.png'
            ),
            User(
                id=17,
                name='Wanessa Camargo',
                instagram_username='wanessa',
                followers=0,
                url_image='https://s2.glbimg.com/3Iqta5qDjRpYO7q3amYfcAY2N0g=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/j/s/lGYei7R0uDnTRdJzIVxA'
                          '/cabecograma-330x270-0005-12-wanessa-camargo.png'
            ),
            User(
                id=18,
                name='Yasmin Brunet',
                instagram_username='yasminbrunet',
                followers=0,
                url_image='https://s2.glbimg.com/vQXTj5pEJpdsT5leoENQ8WbNXrk=/i.s3.glbimg.com/v1'
                          '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2024/T/i/YF72BOQO2QXGWky3avTA'
                          '/cabecograma-330x270-0018-2-yasmin.png'
            ),
            # User(
            #     id=19,
            #     name='Gabriel Santana',
            #     instagram_username='gbielsantana',
            #     followers=profile.from_username(bot.context, 'gbielsantana').followers,
            #     url_image='https://s2.glbimg.com/hnfJZ0wgKyySKyfXqlLX7CwZ7Ug=/i.s3.glbimg.com/v1'
            #               '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/x/p/esEdQlQPmY5U1C2KAGmQ'
            #               '/gabriel-santana-foto-330-270-bbb23.png'
            # ),
            # User(
            #     id=20,
            #     name='Amanda',
            #     instagram_username='ameirelles',
            #     followers=profile.from_username(bot.context, 'ameirelles').followers,
            #     url_image='https://s2.glbimg.com/A40VzPy5Fs8lVKRYSR5m8QDo9Cs=/i.s3.glbimg.com/v1'
            #               '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/l/1/XBiigWR4iH4tA4DoSDnA'
            #               '/amanda-foto-330-270-bbb23.png'
            # ),
            # User(
            #     id=21,
            #     name='Bruno',
            #     instagram_username='brunornogueira',
            #     followers=profile.from_username(bot.context, 'brunornogueira').followers,
            #     url_image='https://s2.glbimg.com/F8GthYiW4DsHxAFe9bVvsz1OGfA=/i.s3.glbimg.com/v1'
            #               '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/w/i/H84f93Qg6mQHwlz3IZ4A'
            #               '/bruno-foto-330-270-bbb23.png'
            # ),
            # User(
            #     id=22,
            #     name='MC Guimê',
            #     instagram_username='mcguime',
            #     followers=profile.from_username(bot.context, 'mcguime').followers,
            #     url_image='https://s2.glbimg.com/_d7OBvTEilzCgRAyQW8rTA3JyP4=/i.s3.glbimg.com/v1'
            #               '/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2023/j/w/07Dl8YRKKoyboVMwXrJw/mc'
            #               '-guime-foto-330-270-bbb23.png'
            # ),
        ]

        for user in users:
            try:
                user.Followers = self.__profile.from_username(self.__bot.context, user.Instagram_username).followers
                print(f'{user.Name} = {user.Followers}')
            except Exception as e:
                print(f'Erro - username "{user.Name}" __ {e}')
                user.followers = 0

        return users
