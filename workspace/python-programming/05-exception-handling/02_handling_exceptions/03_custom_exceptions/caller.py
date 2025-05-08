from xyz import AccessNetwork, InvalidAccessTokenError

if __name__ == '__main__':
    access_network = AccessNetwork()
    try:
        access_network.get_token("Vf")
    except InvalidAccessTokenError:
        print("Check guide")