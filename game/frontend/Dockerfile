# Usando imagem oficial Node LTS
FROM node:18-alpine

# Cria diretório de trabalho
WORKDIR /app

# Copia package.json e package-lock.json
COPY package*.json ./

# Instala dependências
RUN npm install

# Copia todo o restante do código
COPY . .

# Constrói o app para produção
RUN npm run build

# Expõe a porta 3000
EXPOSE 3000

# Comando de inicialização
CMD ["npm", "start"]
