""" Native imports. """
import asyncio

""" Custom imports. """
from obj.dashboard import Dashboard
from obj.scenario import Scenario

""" Throw different exceptions.

@param mes : The exception type
@type mes: String
"""
def throw_exec(mes):

    if (mes == 'main'):
        print("\n\n[!] Error running main function.")
    elif (mes == 'boot'):
        print("\n\n[!] Error booting UI.")

""" Declare/use server object.

@return null
"""
async def main():

    try:
        scenario = Scenario()
        await scenario.reqresolve()
        await scenario.pkgresolve()

        dashboard = Dashboard(scenario, asyncio.get_event_loop())

        while True:
            await asyncio.sleep(3600)

    except Exception as ex:
        throw_exec('boot')

""" Runs the async main function.

@return null
"""
if __name__ == '__main__':

    try:
        asyncio.run(main())
    except asyncio.CancelledError:
        print("\n\n[!] Tasks were cancelled.")
    except KeyboardInterrupt:
        print("\n[!] Server shutdown.")
    except Exception as ex:
        throw_exec('main')