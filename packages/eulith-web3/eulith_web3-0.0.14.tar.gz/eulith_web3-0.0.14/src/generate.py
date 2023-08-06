from eulith_web3.binding_generator import ContractBindingGenerator
import glob

if __name__ == '__main__':
    curve_contracts = glob.glob('../../../contracts/src/main/sol/convex/interfaces/*.sol')
    g = ContractBindingGenerator(curve_contracts, {'@openzeppelin': '../../../node_modules/@openzeppelin'})
    g.generate('hello')