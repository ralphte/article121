// Serves the static holding page. Sends www to the bare domain so there is one canonical address.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === 'www.article121.com') {
      url.hostname = 'article121.com';
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  },
};
