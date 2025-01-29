# Blockchain 

## Description
Your task is to build a simple blockchain from scratch using Python. The blockchain should include core features such as proof-of-work, mining, and transaction validation. This project will help you understand the fundamental concepts of blockchain technology and how it works under the hood.

## Requirements

### Core Features
1. **Blockchain Structure**:
   - Each block should contain:
     - Index
     - Timestamp
     - List of transactions
     - Previous block hash
     - Nonce (for proof-of-work)
     - Current block hash
   - Use cryptographic hashing (e.g., SHA-256) to link blocks.

2. **Proof-of-Work**:
   - Implement a proof-of-work mechanism to mine new blocks.
   - Miners should solve a computational puzzle (e.g., find a hash with a certain number of leading zeros).

3. **Transaction Validation**:
   - Create a system to validate transactions before adding them to a block.
   - Ensure that transactions are signed and cannot be tampered with.

4. **Mining**:
   - Implement a mining function that:
     - Gathers pending transactions.
     - Solves the proof-of-work puzzle.
     - Adds the new block to the blockchain.

### Advanced Features
1. **Wallet System**:
   - Create a wallet system where users can:
     - Generate public/private key pairs.
     - Send and receive "coins" (tokens) securely.
   - Use digital signatures to verify transactions.

2. **Consensus Algorithm**:
   - Implement an alternative consensus algorithm, such as Proof of Stake (PoS), where validators are chosen based on the number of coins they hold.

3. **Network Simulation**:
   - Simulate a peer-to-peer network where multiple nodes can:
     - Share the blockchain.
     - Validate and add new blocks.
   - Handle conflicts using a consensus mechanism (e.g., longest chain rule).

## Expected Outcomes

### Deliverables
1. A Python script or module that implements the blockchain with the core features.
2. A wallet system that allows users to create wallets, send, and receive coins.
3. Documentation explaining how to run the code and interact with the blockchain.

### Code Quality
- Use clean, modular, and well-documented code.
- Include unit tests for critical components (e.g., block validation, proof-of-work).

### Bonus Points
- Implement a simple CLI or web interface to interact with the blockchain.
- Add support for smart contracts or custom tokens.


## Libraries to Use
- `hashlib`: For cryptographic hashing (e.g., SHA-256).
- `datetime`: For timestamping blocks.
- `json`: For serializing block and transaction data.
- `ecdsa` (optional): For generating public/private key pairs and signing transactions.


## Example Workflow
1. Initialize the blockchain with a genesis block.
2. Create wallets for users.
3. Simulate transactions between users.
4. Mine new blocks to add transactions to the blockchain.
5. Validate the blockchain to ensure integrity.


## Resources
- [Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf)
- [Blockchain Basics](https://www.investopedia.com/terms/b/blockchain.asp)
- [Python `hashlib` Documentation](https://docs.python.org/3/library/hashlib.html)
