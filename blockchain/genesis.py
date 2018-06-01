from blockchain import Transaction, TransactionOutput


def get_genesis_transaction(sender_wallet, recipient_wallet, value, all_utxos):
    genesis_transaction = Transaction(
        sender_wallet.public_key_as_str(),
        recipient_wallet.public_key_as_str(),
        value,
        []
    )

    genesis_transaction.generate_signature(sender_wallet.private_key)  # manually sign genesis transaction

    genesis_transaction.transaction_id = "0"  # manually set transaction id

    # manually generate transaction output
    genesis_transaction.outputs.append(TransactionOutput(
        genesis_transaction.recipient,
        genesis_transaction.value,
        genesis_transaction.transaction_id
    ))

    # its important to save our first transaction output in utxos
    all_utxos[genesis_transaction.outputs[0].id] = genesis_transaction.outputs[0]

    return genesis_transaction
