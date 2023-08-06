# pylint:
#
"""
Smash xbar client.  Displays status in format usable for [xbar](xbarapp.com).
"""
import requests
from smash import config
from smash import smash


def xbar():
    """ Interpret Smash node and status information as menus for xbar.
    """
    # load configuration
    # pylint: disable=invalid-name,broad-except
    try:
        conf = config.xbar()
        conf.merge()
    except Exception as e:
        print(f"{config.APP_TAG} | color={smash.state_colours['unknown']}")
        print("---")
        print(f"Could not load Smash configuration: {e}")
        return

    api_url = conf['server'] + '/api'
    timeout = conf['request_timeout']

    # load node and status information
    try:
        nodes = smash.load_nodes(api_url, timeout)
    except requests.exceptions.ConnectionError:
        print(f"{config.APP_TAG} | color={smash.state_colours['unknown']}")
        print("---")
        print("Could not connect to Smash server")
        return

    # now do the BitBar/xbar stuff
    # TODO: move this stuff to APIHandler object?
    # determine and present the overall status in menu bar
    (overall, summary) = smash.overall_state(smash.state_totals)
    colour = smash.state_colours[overall]
    print(f"{config.APP_TAG} | color={colour}")
    print("---")

    # create menu entries for each node and its status items
    for node in nodes:

        # determine overall node status
        (overall, summary) = smash.overall_state(node['totals'])

        # present menu entry for node
        if overall == 'okay':
            print(node['node'])
        else:
            colour = smash.state_colours[overall]
            print(f"{node['node']} {smash.state_icons[overall]} {summary} | color={colour}")

        # build menu of node statuses
        for status in node['statuses']:
            state = status['state']
            message = status['message']
            if 'acknowledgement' in status:
                colour = 'blue'
                icon = ':see_no_evil:'
                message += ' (acknowledged)'
            else:
                colour = smash.state_colours[state]
                icon = smash.state_icons[state]

            if icon:
                print(f"--{icon} {status['test']} "
                      f"{state} {message} | color={colour}")
            else:
                print(f"--{status['test']} {state} {message} | color={colour}")


# if this module was called directly
if __name__ == '__main__':
    xbar()
