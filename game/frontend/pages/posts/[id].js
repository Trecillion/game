import axios from 'axios';

export default function PostDetail({ post }) {
  if (!post) return <p>Carregando...</p>;

  return (
    <div style={{ padding: '1rem' }}>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
}

export async function getServerSideProps(context) {
  const { id } = context.params;
  const res = await axios.get(`https://jsonplaceholder.typicode.com/posts/${id}`);
  return {
    props: {
      post: res.data,
    },
  };
}
