import axios from 'axios';

export default function Posts({ posts }) {
  return (
    <div style={{ padding: '1rem' }}>
      <h1>Lista de Posts (SSR)</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id} style={{ marginBottom: '0.5rem' }}>
      <strong>{post.title}</strong>
      <p>{post.body}</p>
      <a href={`/posts/${post.id}`} style={{ color: 'blue' }}>(Detalhes)</a>
    </li>
        ))}
      </ul>
    </div>
  );
}

// SSR (Server-Side Rendering)
export async function getServerSideProps() {
  const res = await axios.get('https://jsonplaceholder.typicode.com/posts?_limit=5');
  return {
    props: {
      posts: res.data,
    },
  };
}
