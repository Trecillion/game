export default function Layout({ children }) {
  return (
    <div style={{
      margin: '0 auto',
      maxWidth: '800px',
      padding: '1rem'
    }}>
      <header style={{ marginBottom: '2rem' }}>
        <h1>Meu Site Next.js</h1>
        <nav>
          <a href="/" style={{ marginRight: '1rem', color: 'blue' }}>Home</a>
          <a href="/posts" style={{ marginRight: '1rem', color: 'blue' }}>Posts</a>
          <a href="/dashboard" style={{ color: 'blue' }}>Dashboard</a>
        </nav>
      </header>

      <main>{children}</main>

      <footer style={{ marginTop: '2rem', borderTop: '1px solid #ccc', paddingTop: '1rem' }}>
        <p>© 2023 - Meu Projeto Next.js</p>
      </footer>
    </div>
  );
}
