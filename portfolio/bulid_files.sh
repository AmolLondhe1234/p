# {
# #   "$schema": "https://openapi.vercel.sh/vercel.json",
#   "version": 2,
#   "rewrites": [
#     {
#       "src": "portfolio/wsgi.py",
#       "use": "@vercel/python",
#       "config":{"maxLambadaSize":"15mb","runtime":"python3.10"}
#     },
#     {
#     "src": "build_files.sh",
#     "use": "@vercel/static-build",
#     "config":{
#         "distDir": "staticdiles_build"
#     }
#     }
#   ],
#   "routers": [
#     {
#       "src": "/static/(.*)",
#       "dest": "/static/$1"
#     },
#     {
#         "src":"/(.*)",
#         "dest":"portfolio/wsgi.py"
#     }
#   ],
# }
echo "BUILD START"
python3.10 -m pip install -r requirements.txt
python3.10 manage.py collectstatic --noinput --clear
