#!/usr/bin/env python3
import os
import json
import sys

# Ajuste aqui para o caminho onde fica a pasta "game", que já contém "frontend".
# Neste caso, você informou: C:\Users\escal\OneDrive\Documents\Project\Gamify\game
ROOT_DIR = r"C:\Users\escal\OneDrive\Documents\Project\Gamify\game"
BACKEND_FOLDER_NAME = "backend"

def create_backend_folder():
    """
    Tenta criar a pasta 'backend' dentro de ROOT_DIR.
    Se ocorrer PermissionError ou algo assim, pergunta ao usuário o que fazer.
    Retorna:
      - backend_path (str): caminho completo para a pasta 'backend'
      - folder_exists (bool): indica se a pasta realmente existe
    """
    backend_path = os.path.join(ROOT_DIR, BACKEND_FOLDER_NAME)
    folder_exists = False

    try:
        os.makedirs(backend_path, exist_ok=True)
        print(f"[INFO] Pasta {backend_path} criada ou já existia.")
        folder_exists = True
    except PermissionError as e:
        print(f"[ERRO] Permissão negada ao criar {backend_path}: {e}")
        print("[OPÇÕES]:")
        print("  1) Mudar o caminho ROOT_DIR no script e rodar novamente")
        print("  2) Continuar sem criar a pasta (assumindo que ela já exista)")
        choice = input("Escolha [1/2]: ").strip()

        if choice == "1":
            print("\n[AVISO] Ajuste a variável ROOT_DIR no script e rode novamente.")
            sys.exit(1)
        else:
            # Se a pasta já existir, beleza; senão, aborta.
            if os.path.isdir(backend_path):
                folder_exists = True
                print("[INFO] A pasta já existe. Continuando...")
            else:
                print("[ERRO] A pasta não existe. Crie manualmente e rode o script novamente.")
                sys.exit(1)

    return backend_path, folder_exists

def create_package_json(backend_path):
    """ Cria um package.json básico para Node.js + Express + pg (Postgres). """
    package_data = {
        "name": "gamify_backend",
        "version": "1.0.0",
        "main": "index.js",
        "scripts": {
            "dev": "nodemon index.js",
            "start": "node index.js"
        },
        "dependencies": {
            "express": "latest",
            "pg": "latest",
            "dotenv": "latest"
        },
        "devDependencies": {
            "nodemon": "latest"
        }
    }

    package_json_path = os.path.join(backend_path, "package.json")
    with open(package_json_path, "w", encoding="utf-8") as f:
        json.dump(package_data, f, indent=2)
    print(f"[INFO] Criado package.json em {package_json_path}")

def create_index_js(backend_path):
    """ Cria um index.js com servidor Express usando Postgres. """
    index_js_path = os.path.join(backend_path, "index.js")
    content = r"""require('dotenv').config();
const express = require('express');
const { Pool } = require('pg');

const app = express();
app.use(express.json());

// Configurações de conexão com Postgres
// Variáveis de ambiente em .env:
//   PGHOST, PGUSER, PGPASSWORD, PGDATABASE, PGPORT
const pool = new Pool({
  host: process.env.PGHOST || 'localhost',
  user: process.env.PGUSER || 'postgres',
  password: process.env.PGPASSWORD || 'postgres',
  database: process.env.PGDATABASE || 'gamify_db',
  port: process.env.PGPORT || 5432
});

// Rota de teste
app.get('/', async (req, res) => {
  try {
    const result = await pool.query('SELECT NOW() AS current_time');
    res.json({
      message: 'Hello from Express + Postgres!',
      dbTime: result.rows[0].current_time
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Erro ao consultar o banco de dados' });
  }
});

// Porta padrão
const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
"""

    with open(index_js_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[INFO] Criado index.js em", index_js_path)

def create_dotenv_example(backend_path):
    """ Cria .env.example com placeholders para Postgres. """
    dotenv_example_path = os.path.join(backend_path, ".env.example")
    content = """\
# Exemplo de variáveis de ambiente para conectar ao Postgres
PGHOST=localhost
PGUSER=postgres
PGPASSWORD=postgres
PGDATABASE=gamify_db
PGPORT=5432

# Porta do servidor Express
PORT=4000
"""
    with open(dotenv_example_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[INFO] Criado .env.example em {dotenv_example_path}")

def create_gitignore(backend_path):
    """ Cria um .gitignore básico para Node + Express + Postgres. """
    gitignore_content = """\
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Ambiente
.env
*.env

# Dependências
node_modules/
.pnpm-store/

# Build
dist/
build/

# Sistema
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
"""
    gitignore_path = os.path.join(backend_path, ".gitignore")
    with open(gitignore_path, "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print("[INFO] Criado .gitignore em", gitignore_path)

def main():
    print("=== CRIADOR DE BACKEND COM POSTGRES ===")
    backend_path, folder_exists = create_backend_folder()

    if not folder_exists:
        print("[ERRO] Pasta backend não disponível. Encerrando.")
        sys.exit(1)

    create_package_json(backend_path)
    create_index_js(backend_path)
    create_dotenv_example(backend_path)
    create_gitignore(backend_path)

    print("\n[INFO] Finalizado!")
    print(f"1) Entre em: {backend_path}")
    print("2) Rode: npm install (ou yarn) para instalar dependências.")
    print("3) Copie .env.example para .env e ajuste as variáveis (PGHOST, PGUSER etc.).")
    print("4) Rode: npm run dev (ou yarn dev) para subir o servidor em http://localhost:4000.")


if __name__ == "__main__":
    main()
