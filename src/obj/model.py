import asyncio

class Model():
    def __init__(self, dashboard, loop):
        self.dashboard = dashboard
        self.loop = loop

        self.path = ''
        self.name = ''
        self.type = ''

    def get_dashboard(self):
        return self.dashboard

    def set_dashboard(self, dashboard):
        self.dashboard = dashboard

    def get_loop(self):
        return self.loop

    def set_loop(self, loop):
        self.loop = loop

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def throw_exec(self, mes):
        if (mes == 'eval'):
            print('[ERR] Error evaluating chosen file.')

    async def describe(self):
        await self.get_dashboard().get_window().get_viewer().clear_lines()
        await self.get_dashboard().get_window().get_viewer().add_line(f'[-->] {self.get_name()} chosen ...')
        await self.get_dashboard().get_window().get_viewer().add_line('')
        await self.get_dashboard().get_window().get_viewer().add_line(f'Select an analytics path above.')


    async def eval(self):
        try:
            async def prove(name):
                tmp = name.split('.')
                if (len(tmp) > 2):
                    return
                else:
                    self.set_name(tmp[0])
                    self.set_type(tmp[1])

                    await self.describe()
                    await self.get_dashboard().get_window().get_emoter().reset()
                    await self.get_dashboard().get_window().get_emoter().emote('aps')

            tmp = self.get_path().split('/')
            sz = len(tmp)
            chosen = tmp[sz-1]
            await prove(chosen)

        except Exception as ex:
            print(ex)
            self.throw_exec('eval')