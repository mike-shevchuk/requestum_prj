from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

import algo


INDEX_HTML = open('index.html', 'rb').read()


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        req = urlparse(self.path)
        if   req.path == '/':                             self.handle_get_index()
        elif req.path == '/api/get_most_similar_repos':   self.handle_get_most_similar_repos(req.query)
        else:                                             self.handle_page_not_found()

    def handle_get_index(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(INDEX_HTML)

    def handle_get_most_similar_repos(self, query_str):
        # TODO: validate user args
        query = parse_qs(query_str)
        repo_url = query['repo_url'][0]  # repo_url is like 'https://github.com/encode/starlette'
        path = urlparse(repo_url).path  # path is like '/encode/starlette'
        path_parts = path.split('/')  # path_parts is ['', 'encode', 'starlette']
        user, repo = path_parts[1], path_parts[2]  # works even if path contains extra shit after repo name like https://github.com/encode/starlette/blob/master/pyproject.toml
        if repo.endswith('.git'):  # remove `.git` from repo name if someone (incorrectly) gave it
            repo = repo[:-4]

        res = algo.get_most_similar_repos(user, repo)

        to_link = lambda s: f"<a href='https://github.com/{s}'>{s}</a>"
        contribs_to_str = lambda contribs: ', '.join(map(to_link, contribs))

        items_str = '\n'.join([f'<li>{to_link(repo)}: {len(contribs)} common contributor(s): {contribs_to_str(contribs)}</li>' for repo, contribs in res])
        page = f'<h2>Similar to {to_link(repo)}</h2><ul>{items_str}</ul>'

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(page.encode('utf-8'))

        # TODO for next version: stream results as they are being computed

    def handle_page_not_found(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Not found')


def start_web_server(addr, port):
    print(f'Starting web server on {addr}:{port} ...', end='', flush=True)
    httpd = ThreadingHTTPServer((addr, port), RequestHandler)
    try:
        print(' done!')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
