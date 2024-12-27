import NextAuth from "next-auth";
import GithubProvider from "next-auth/providers/github";
// Se quiser Google, use: import GoogleProvider from "next-auth/providers/google";

export default NextAuth({
  // Configure um ou mais providers de login
  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_CLIENT_ID,
      clientSecret: process.env.GITHUB_CLIENT_SECRET
    }),
    // GoogleProvider({
    //   clientId: process.env.GOOGLE_CLIENT_ID,
    //   clientSecret: process.env.GOOGLE_CLIENT_SECRET
    // })
  ],
  // Se quiser customizar páginas de login, callbacks, etc., configure aqui.
  // Exemplo:
  // pages: {
  //   signIn: '/auth/signin',
  // }
});
