from eulith_web3.erc20 import TokenSymbol
from eulith_web3.eulith_web3 import EulithWeb3
from eulith_web3.requests import EulithShortOnRequest, EulithShortOffRequest, EulithAaveV2StartLoanRequest, \
    EulithAaveV2InnerLoanBody, FlashRequest
from eulith_web3.signing import construct_signing_middleware, LocalSigner


# all these tests require running devrpc
from eulith_web3.uniswap import EulithUniV3StartLoanRequest, EulithUniswapPoolLookupRequest, UniswapPoolFee


def test_v0_get_contract():
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    contract_address = ew3.v0.get_toolkit_contract_address(acct.address)
    print(f'contract address: {contract_address}')


def test_v0_erc_lookup():
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    erc = ew3.v0.get_erc_token(TokenSymbol.WETH)
    assert erc.address == '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'


def test_v0_create_contract():
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    acct = LocalSigner("0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d")
    ew3.v0.create_toolkit_contract(acct.address)


def test_v0_create_contract_if_not_exists():
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    acct = LocalSigner("0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80")
    assert ew3.v0.ensure_toolkit_contract(acct.address) == ew3.v0.ensure_toolkit_contract(acct.address)


def test_v0_multi_transfer():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    one = LocalSigner("0x1deff2733e6142c873df7bede7db29055471ebeae7090ef618996a51daa4cd8c")
    two = LocalSigner("0x2deff2733e6142c873df7bede7db29055471ebeae7090ef618996a51daa4cd8c")
    three = LocalSigner("0x3deff2733e6142c873df7bede7db29055471ebeae7090ef618996a51daa4cd8c")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    ew3.v0.ensure_toolkit_contract(acct.address)
    b1_before = ew3.eth.get_balance(one.address)
    b2_before = ew3.eth.get_balance(two.address)
    b3_before = ew3.eth.get_balance(three.address)
    ew3.v0.start_atomic_transaction(acct.address)
    ew3.eth.send_transaction({'from': acct.address, 'to': one.address, 'value': 12131415})
    ew3.eth.send_transaction({'from': acct.address, 'to': two.address, 'value': 22131415})
    ew3.eth.send_transaction({'from': acct.address, 'to': three.address, 'value': 32131415})
    assert b1_before == ew3.eth.get_balance(one.address)
    txparams = ew3.v0.commit_atomic_transaction()
    tx = ew3.eth.send_transaction(txparams)
    ew3.eth.wait_for_transaction_receipt(tx)
    assert b1_before + 12131415 == ew3.eth.get_balance(one.address)
    assert b2_before + 22131415 == ew3.eth.get_balance(two.address)
    assert b3_before + 32131415 == ew3.eth.get_balance(three.address)


def test_v0_refresh_api_token():
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     )
    assert ew3.eth.chain_id == 31337
    ew3.v0.refresh_api_token()
    assert ew3.eth.chain_id == 31337


def test_short_on_off_request():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    collateral_token = ew3.v0.get_erc_token(TokenSymbol.USDC)
    short_token = ew3.v0.get_erc_token(TokenSymbol.WETH)
    collateral_amount = 1000

    transfer_collateral_to_contract = collateral_token.transfer(
        proxy_address, int(collateral_amount * 1.2 * 10**collateral_token.decimals),
        {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(transfer_collateral_to_contract)

    contract_balance = collateral_token.balance_of(proxy_address)
    assert contract_balance >= collateral_amount * 10**collateral_token.decimals

    short_on_params = EulithShortOnRequest(
        collateral_token=collateral_token,
        short_token=short_token,
        collateral_amount=collateral_amount)

    ew3.v0.start_atomic_transaction(account=acct.address)
    leverage = ew3.v0.short_on(short_on_params)
    assert leverage > 5

    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    short_off_params = EulithShortOffRequest(
        collateral_token=collateral_token,
        short_token=short_token,
        repay_short_amount=0.01,
        true_for_unwind_a=True
    )

    ew3.v0.start_atomic_transaction(account=acct.address)
    released_collateral = ew3.v0.short_off(short_off_params)
    assert released_collateral > 10
    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    short_off_params_b = EulithShortOffRequest(
        collateral_token=collateral_token,
        short_token=short_token,
        repay_short_amount=0.01,
        true_for_unwind_a=False
    )

    ew3.v0.start_atomic_transaction(account=acct.address)
    released_collateral = ew3.v0.short_off(short_off_params_b)
    assert released_collateral > 10
    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1


def test_start_uniswap_v3_loan():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    borrow_token = ew3.v0.get_erc_token(TokenSymbol.USDC)
    borrow_token_b = ew3.v0.get_erc_token(TokenSymbol.WETH)

    bor_amt_a = 10
    bor_amt_b = 3

    tx = borrow_token.approve(proxy_address, int(bor_amt_a*1.2*10**borrow_token.decimals), {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    tx = borrow_token_b.approve(proxy_address, int(bor_amt_b*1.2*10**borrow_token_b.decimals), {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    contract_balance_before = borrow_token.balance_of(proxy_address)
    contract_balance_b_before = borrow_token_b.balance_of(proxy_address)

    start_loan_request = EulithUniV3StartLoanRequest(
        borrow_token_a=borrow_token,
        borrow_amount_a=bor_amt_a,
        borrow_token_b=borrow_token_b,
        borrow_amount_b=bor_amt_b,
        pay_transfer_from=acct.address,
        recipient=proxy_address
    )

    ew3.v0.start_atomic_transaction(account=acct.address)
    ew3.v0.start_flash_loan(start_loan_request)
    tx_count = ew3.v0.finish_inner()
    assert tx_count == 1

    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    contract_balance_after = borrow_token.balance_of(proxy_address)
    assert contract_balance_after - contract_balance_before == bor_amt_a*10**borrow_token.decimals
    contract_balance_b_after = borrow_token_b.balance_of(proxy_address)
    assert contract_balance_b_after - contract_balance_b_before == bor_amt_b*10**borrow_token_b.decimals


def test_start_aave_v3_loan():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    borrow_token = ew3.v0.get_erc_token(TokenSymbol.USDC)
    borrow_token_b = ew3.v0.get_erc_token(TokenSymbol.WETH)

    bor_amt_a = 10
    bor_amt_b = 1

    transfer_collateral_to_contract = borrow_token.transfer(
        proxy_address, int(bor_amt_a * 1.2 * 10 ** borrow_token.decimals),
        {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(transfer_collateral_to_contract)

    transfer_collateral_to_contract_b = borrow_token_b.transfer(
        proxy_address, int(bor_amt_a * 1.2 * 10 ** borrow_token_b.decimals),
        {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(transfer_collateral_to_contract_b)

    contract_balance_before = borrow_token.balance_of(proxy_address)
    contract_balance_b_before = borrow_token_b.balance_of(proxy_address)

    start_loan_request = EulithAaveV2StartLoanRequest(
        tokens=[
            EulithAaveV2InnerLoanBody(
                token_address=borrow_token,
                amount=bor_amt_a),
            EulithAaveV2InnerLoanBody(
                token_address=borrow_token_b,
                amount=bor_amt_b),
        ]
    )

    ew3.v0.start_atomic_transaction(account=acct.address)
    ew3.v0.start_flash_loan(start_loan_request)
    tx_count = ew3.v0.finish_inner()
    assert tx_count == 1

    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    contract_balance_after = borrow_token.balance_of(proxy_address)
    assert contract_balance_after - contract_balance_before == -9000  # the fee for taking an aave loan
    contract_balance_b_after = borrow_token_b.balance_of(proxy_address)
    assert contract_balance_b_after - contract_balance_b_before == -900000000000000  # the fee for taking an aave loan


def test_start_uniswap_v3_swap():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    token_a = ew3.v0.get_erc_token(TokenSymbol.USDC)
    token_b = ew3.v0.get_erc_token(TokenSymbol.WETH)
    sell_amount = 10

    buy_balance_before = token_b.balance_of(proxy_address)

    # approve the transfer from the wallet to cover the sell side of the swap
    tx = token_a.approve(proxy_address, int(sell_amount * 1.2 * 10 ** token_a.decimals),
                         {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    price, fee, req = ew3.v0.get_univ3_best_price_quote(token_a, token_b, sell_amount, pay_transfer_from=acct.address)

    ew3.v0.start_atomic_transaction(account=acct.address)
    ew3.v0.start_uni_swap(req)
    tx_count = ew3.v0.finish_inner()
    assert tx_count == 1

    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    buy_balance_after = token_b.balance_of(proxy_address)

    assert int((buy_balance_after - buy_balance_before) / 100) \
           == int((sell_amount / price) * 10**token_b.decimals / 100)


def test_nested_txs():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    borrow_token = ew3.v0.get_erc_token(TokenSymbol.USDC)
    borrow_token_b = ew3.v0.get_erc_token(TokenSymbol.WETH)

    bor_amt_a = 100
    bor_amt_b = 3

    tx = borrow_token.approve_float(proxy_address, bor_amt_a * 1.2, {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    tx = borrow_token_b.approve_float(proxy_address, bor_amt_b * 1.2, {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    contract_balance_before = borrow_token.balance_of(proxy_address)
    contract_balance_b_before = borrow_token_b.balance_of(proxy_address)

    start_loan_request = EulithUniV3StartLoanRequest(
        borrow_token_a=borrow_token,
        borrow_amount_a=bor_amt_a,
        borrow_token_b=borrow_token_b,
        borrow_amount_b=bor_amt_b,
        pay_transfer_from=acct.address,
        recipient=proxy_address
    )

    ew3.v0.start_atomic_transaction(account=acct.address)
    fee = ew3.v0.start_flash_loan(start_loan_request)
    assert fee == 0.0005

    pool = ew3.v0.get_univ3_pool(EulithUniswapPoolLookupRequest(
        token_a=borrow_token,
        token_b=borrow_token_b,
        fee=UniswapPoolFee.ThirtyBips))

    price, fee, req = pool.get_quote(borrow_token, bor_amt_a)
    ew3.v0.start_uni_swap(req)

    tx_count = ew3.v0.finish_inner()
    assert tx_count == 0  # count doesn't increment because we still haven't closed the outer tx

    tx_count = ew3.v0.finish_inner()
    assert tx_count == 1

    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    contract_balance_after = borrow_token.balance_of(proxy_address)
    assert contract_balance_after == contract_balance_before  # we swapped the full amount away

    contract_balance_b_after = borrow_token_b.balance_of(proxy_address)
    assert int((contract_balance_b_after - contract_balance_b_before) / 100) == \
           int((int(bor_amt_b * 10**borrow_token_b.decimals)
               + int((bor_amt_a / price) * 10**borrow_token_b.decimals)) / 100)


def test_univ3_best_price_quote():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))
    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    sell_token = ew3.v0.get_erc_token(TokenSymbol.USDC)
    buy_token = ew3.v0.get_erc_token(TokenSymbol.WETH)

    sell_amount = 100

    contract_balance_before = buy_token.balance_of_float(proxy_address)

    price, fee, req = ew3.v0.get_univ3_best_price_quote(sell_token, buy_token, sell_amount)

    tx = sell_token.transfer_float(proxy_address, sell_amount*1.05, {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    ew3.v0.start_atomic_transaction(account=acct.address)
    ew3.v0.start_uni_swap(req)
    tx_count = ew3.v0.finish_inner()
    assert tx_count == 1

    tx = ew3.v0.commit_atomic_transaction()

    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    contract_balance_after = buy_token.balance_of_float(proxy_address)

    assert round((contract_balance_after - contract_balance_before), 6) == round(sell_amount / price, 6)


def test_flash_pay_flash_logic_different_tokens():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))

    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    pay_token = ew3.v0.get_erc_token(TokenSymbol.USDC)
    take_token = ew3.v0.get_erc_token(TokenSymbol.WETH)

    take_amount = 2
    # # magic number math to cover enough USDC to pay back the ETH and max $1,500 per.
    pay_amount = take_amount * 1500 * 1.2
    tx = pay_token.approve_float(proxy_address, pay_amount, {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    flash_params = FlashRequest(take=take_token, pay=pay_token, take_amount=take_amount,
                                pay_transfer_from=ew3.toChecksumAddress(acct.address))

    ew3.v0.start_atomic_transaction(account=acct.address)
    price, fee = ew3.v0.start_flash(flash_params)
    assert 1000 < price < 2000  # assert price is reasonable
    assert fee == 0.0005

    tx_num = ew3.v0.pay_flash()
    assert tx_num == 1
    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000

    take_token_balance_before = take_token.balance_of_float(proxy_address)

    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    take_token_balance_after = take_token.balance_of_float(proxy_address)

    assert take_token_balance_after - take_token_balance_before == take_amount


def test_flash_pay_flash_logic_same_tokens():
    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))

    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)
    pay_token = ew3.v0.get_erc_token(TokenSymbol.USDC)

    take_amount = 2

    tx = pay_token.approve_float(proxy_address, take_amount * 1.2, {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    flash_params = FlashRequest(take=pay_token, pay=pay_token, take_amount=take_amount,
                                pay_transfer_from=ew3.toChecksumAddress(acct.address))

    ew3.v0.start_atomic_transaction(account=acct.address)
    price, fee = ew3.v0.start_flash(flash_params)
    assert price == 1
    assert fee == 0.0005

    tx_num = ew3.v0.pay_flash()
    assert tx_num == 1
    tx = ew3.v0.commit_atomic_transaction()
    tx['gas'] = 1000000

    take_token_balance_before = pay_token.balance_of_float(proxy_address)

    tx_hash = ew3.eth.send_transaction(tx)
    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    take_token_balance_after = pay_token.balance_of_float(proxy_address)

    assert take_token_balance_after - take_token_balance_before == take_amount
