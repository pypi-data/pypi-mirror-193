function try_node() {
    if [[ -f "$NVM_DIR/nvm.sh" ]]
        then source $NVM_DIR/nvm.sh
        else exit "Missing dependence: NVM"
    fi

    code .

    if [[ -f ".nvmrc" ]]
        then echo "using .nvmrc" && nvm use
        else echo "'.nvmrc' not found, using LTS" && nvm use --lts
    fi

    if [[ -d "node_modules" ]]
        then echo "node_modules alredy installed, running dev server"
        else echo "Downloading node_modules..." && npx yarn
    fi

    npx yarn dev
}
