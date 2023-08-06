import os
import web3
from web3.types import TxParams

from eulith_web3.erc20 import TokenSymbol
from eulith_web3.eulith_web3 import EulithWeb3, EulithRpcException
from eulith_web3.swap import EulithSwapProvider, EulithSwapRequest, EulithLiquiditySource
from eulith_web3.signing import construct_signing_middleware, LocalSigner
from fixture.swap import run_one_swap, run_one_call_to_swap

EULITH_URL = os.environ.get("EULITH_URL", default="http://localhost:7777/v0")


# all these tests require running devrpc

def test_acct_on_smw():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    smw = construct_signing_middleware(acct)
    print(smw.address)


def test_local_chain_id():
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    assert ew3.eth.chain_id == 31337


def test_account_bal():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct)
                     )
    balance = ew3.eth.get_balance(acct.address)
    assert balance > 1000


def test_get_contract():
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    contract_address = ew3.eulith_contract_address(acct.address)
    print(f'contract address: {contract_address}')


def test_erc_lookup():
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    erc = ew3.eulith_get_erc_token(TokenSymbol.WETH)
    assert erc.address == '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'


def test_create_contract():
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3.eulith_create_contract(acct.address)


def test_create_contract_if_not_exists():
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    assert ew3.eulith_create_contract_if_not_exist(acct.address) == ew3.eulith_create_contract_if_not_exist(
        acct.address)


def test_simple_transfer():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    other = LocalSigner("0xddeff2733e6142c873df7bede7db29055471ebeae7090ef618996a51daa4cd8c")
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct)
                     )
    bal_before = ew3.eth.get_balance(other.address)
    txparams = TxParams({'from': acct.address, 'to': other.address, 'value': 12345678})
    tx = ew3.eth.send_transaction(txparams)
    ew3.eth.wait_for_transaction_receipt(tx)
    bal_after = ew3.eth.get_balance(other.address)
    assert bal_after - bal_before == 12345678


def test_multi_transfer():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    one = LocalSigner("0x1deff2733e6142c873df7bede7db29055471ebeae7090ef618996a51daa4cd8c")
    two = LocalSigner("0x2deff2733e6142c873df7bede7db29055471ebeae7090ef618996a51daa4cd8c")
    three = LocalSigner("0x3deff2733e6142c873df7bede7db29055471ebeae7090ef618996a51daa4cd8c")
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    ew3.eulith_create_contract_if_not_exist(acct.address)
    b1_before = ew3.eth.get_balance(one.address)
    b2_before = ew3.eth.get_balance(two.address)
    b3_before = ew3.eth.get_balance(three.address)
    ew3.eulith_start_transaction(acct.address)
    ew3.eth.send_transaction({'from': acct.address, 'to': one.address, 'value': 12131415})
    ew3.eth.send_transaction({'from': acct.address, 'to': two.address, 'value': 22131415})
    ew3.eth.send_transaction({'from': acct.address, 'to': three.address, 'value': 32131415})
    assert b1_before == ew3.eth.get_balance(one.address)
    txparams = ew3.eulith_commit_transaction()
    tx = ew3.eth.send_transaction(txparams)
    ew3.eth.wait_for_transaction_receipt(tx)
    assert b1_before + 12131415 == ew3.eth.get_balance(one.address)
    assert b2_before + 22131415 == ew3.eth.get_balance(two.address)
    assert b3_before + 32131415 == ew3.eth.get_balance(three.address)


def test_refresh_api_token():
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    assert ew3.eth.chain_id == 31337
    ew3.eulith_refresh_api_token()
    assert ew3.eth.chain_id == 31337


def test_swap_route_through_zero_ex():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x8Ef090678C0B80F6F4aD8B5300Ccd41d22940968')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)
    run_one_swap(recipient, EulithSwapProvider.ZERO_EX, signer_middleware)


def test_swap_route_through_one_inch():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)
    run_one_swap(recipient, EulithSwapProvider.ONE_INCH, signer_middleware)


def test_swap_non_atomic():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0xA03D1c3A6954Be49115605Ce9a0b46cb9d7f3517')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     signing_middle_ware=signer_middleware,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw")

    # Want more than 1 deployed contract to test for auth_address inference
    ew3.eulith_create_contract(recipient)

    run_one_swap(recipient, EulithSwapProvider.ONE_INCH, signer_middleware, False)


def test_deposit_withdraw_weth():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url=EULITH_URL,
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))

    weth = ew3.eulith_get_erc_token(TokenSymbol.WETH)
    starting_balance = weth.balance_of(acct.address)

    dep_tx = weth.deposit_eth(1.0)
    dep_tx['from'] = acct.address
    ew3.eth.send_transaction(dep_tx)

    after_deposit_balance = weth.balance_of(acct.address)
    assert int((after_deposit_balance - starting_balance) / 1e18) == 1

    before_withdraw_eth_bal = ew3.eth.get_balance(acct.address)

    withdraw_tx = weth.withdraw_eth(1.0)
    withdraw_tx['from'] = acct.address
    ew3.eth.send_transaction(withdraw_tx)

    after_withdraw_eth_bal = ew3.eth.get_balance(acct.address)
    after_withdraw_balance = weth.balance_of(acct.address)

    assert after_withdraw_balance == starting_balance
    assert 0.99 < (after_withdraw_eth_bal - before_withdraw_eth_bal) / 1e18 < 1.0  # we lose some gas here


def test_call_swap_invalid_slippage_oi():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    try:
        run_one_call_to_swap(recipient, EulithSwapProvider.ONE_INCH, None, 1.5, signer_middleware)
        assert False
    except EulithRpcException:
        assert True


def test_call_swap_invalid_slippage_zx():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    try:
        run_one_call_to_swap(recipient, EulithSwapProvider.ZERO_EX, None, 1.5, signer_middleware)
        assert False
    except EulithRpcException:
        assert True


def test_call_swap_valid_slippage_oi():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    run_one_call_to_swap(recipient, EulithSwapProvider.ONE_INCH, None, 0.02, signer_middleware)


def test_call_swap_valid_slippage_zx():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    run_one_call_to_swap(recipient, EulithSwapProvider.ZERO_EX, None, 0.02, signer_middleware)


def test_call_swap_unexpected_liquidity_source_from_server_oi():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    try:
        run_one_call_to_swap(recipient, EulithSwapProvider.ONE_INCH, EulithLiquiditySource.UNISWAP_V3, 0.02,
                             signer_middleware)
        assert False
    except EulithRpcException:
        assert True


def test_call_swap_unexpected_liquidity_source_from_server_zx():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    try:
        run_one_call_to_swap(recipient, EulithSwapProvider.ZERO_EX, EulithLiquiditySource.UNISWAP_V3, 0.02,
                             signer_middleware)
        assert False
    except EulithRpcException:
        assert True


def test_call_swap_expected_liquidity_source_from_server_oi():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    run_one_call_to_swap(recipient, EulithSwapProvider.ONE_INCH, EulithLiquiditySource.UNISWAP_V2, 0.02,
                         signer_middleware)


def test_call_swap_expected_liquidity_source_from_server_zx():
    w3 = web3.Web3()
    recipient = w3.toChecksumAddress('0x47256A41027e94d1141Dd06f05DcB3ddE0421551')
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    signer_middleware = construct_signing_middleware(acct)

    run_one_call_to_swap(recipient, EulithSwapProvider.ZERO_EX, EulithLiquiditySource.CURVE_V2, 0.02,
                         signer_middleware)