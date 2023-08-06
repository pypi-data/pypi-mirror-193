"""
Need py3.7 min to run pytest
"""
import assetic


class Setup(object):
    def __init__(self):
        self._api_client = None

    @property
    def api_client(self):
        return self._api_client

    @api_client.setter
    def api_client(self, value):
        self._api_client = value

    def init_asseticsdk(self):
        """
        Test initialising the SDK
        Assumes default settings
        :return: True unless exception
        """
        try:
            asseticsdk = assetic.AsseticSDK()
        except Exception as ex:
            raise ex
        self.api_client = asseticsdk.client
        return True

    def test_version_api(self):
        """
        Test version API by ensuring there is a response
        :return: True unless exception
        """
        version_api = assetic.VersionApi(api_client=self.api_client)
        try:
            response = version_api.version_get()
        except Exception as ex:
            print(ex)
            return False
        if "Major" not in response or response["Major"] < 2023:
            print("Major Version not found")
            return False
        print("Assetic Version: {0}.{1}.{2}.{3}".format(
            response["Major"], response["Minor"], response["Build"]
            , response["Revision"]))
        return True


class AssetTests(object):
    def __init__(self, api_client):
        self.assets_api = assetic.AssetApi(api_client=api_client)
        self.asset_tools = assetic.AssetTools(api_client=api_client)
        self.asset_id = None

    def get_assets(self):
        attributes = ["Zone"]
        try:
            response = self.assets_api.asset_get_0(attributes)
        except Exception as ex:
            raise ex

        if response["TotalResults"] > 0:
            self.asset_id = response["ResourceList"][0]["AssetId"]
        return True

    def get_complete_asset(self):
        if not self.asset_id:
            # no asset data to work with
            return True

        attributes = ["Zone"]
        inclusions = ["components", "dimensions", "service_criteria"]

        asset = self.asset_tools.get_complete_asset(
            assetid=self.asset_id, attributelist=attributes
            , inclusions=inclusions)
        if not asset:
            return False
        return True


# initiate setup class
setup_tests = Setup()
setup_tests.init_asseticsdk()
# check we have a api_client setting
if setup_tests.api_client.configuration.password == "" or \
        setup_tests.api_client.configuration.host == "https://xxx.assetic.net":
    raise Exception("Package test authorisation not set")

# initiate SDK to set client
# setup_tests.init_asseticsdk()
# Initiate other classes.
asset_tests = AssetTests(setup_tests.api_client)


def test_setup():
    """
    test initialisation of sdk
    """
    assert setup_tests.init_asseticsdk()


def test_version():
    """
    test version API, fails if unable to get Assetic version
    """
    assert setup_tests.test_version_api()


def test_asset_collection_get():
    """
    test the asset GET collection API
    """
    assert asset_tests.get_assets()


def test_get_complete_asset():
    """
    test the tool get complete asset using an asset from
    the result of test_asset_collection_get
    """
    assert asset_tests.get_complete_asset()
