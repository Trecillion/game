require('dotenv').config();
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
