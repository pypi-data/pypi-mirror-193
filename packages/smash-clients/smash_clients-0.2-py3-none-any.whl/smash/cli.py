# pylint:
#
"""
Smash command-line interface client.
"""
from smash import config
from smash import smash


def json_result(result):
    """ Print result as JSON. """
    print("<< JSON result >>")
    print(result)


def json_error(errmsg):
    """ Print error as JSON. """
    print(f'"error":"{errmsg}"')


def print_result(result):
    """ Print result as text. """
    # DO something different
    print("<< plaintext result >>")
    print(result)


def print_error(errmsg):
    """ Print error as text. """
    print(f"Error: {errmsg}")


def main():
    """ Main client routine. """

    # load configuration
    # pylint: disable=invalid-name,broad-except
    try:
        conf = config.cli()
        args = conf.argparser.parse_args()
        conf.merge()
    except Exception as e:
        print(f"Could not load Smash configuration: {e}")
        return

    api = smash.ApiHandler(conf)

    print(f"Args: {vars(args)}")

    # for collecting output and result
    output = None

    # DO put this next section in a try..except thingy (maybe)
    # the idea being to capture any exceptions and output them appropriately

    # handle command
    if args.cmd == 'get':

        output = []
        for ns in args.nodestatus:
            if ns[1]:
                output.append(api.get_node_status(ns[0], ns[1]))
            else:
                output.append(api.get_node(ns[0]))

#    elif args.cmd in ['del, 'delete']:
#
#        node = args.nodestatus[0]
#        status = args.nodestatus[1]
#        if node and status:
#            output = api.delete_node_status(node, status)
#        elif node:
#            output = api.delete_node(node)

    elif args.cmd in ['ack', 'acknowledge']:
        output = api.acknowledge(args.nodestatus[0], args.nodestatus[1],
            args.message, args.state, args.expire_after)

    else:
        print_error(f"Not recognized: command {args.cmd}")

    # handle output
    if not output:
        if args.json:
            json_error(f"This sucks: {args.cmd} unsuccessful")
        else:
            print_error(f"This sucks: {args.cmd} unsuccessful")
    else:
        if args.json:
            json_result(output)
        else:
            print_result(output)


# if this module was called directly
if __name__ == '__main__':
    main()
