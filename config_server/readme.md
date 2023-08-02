# Trace de la configuration du serveur JupyterHub

# Création d'un conteneur lxd
1. Création du conteneur `lxc launch ubuntu:22.04 jupyterhub`
2. Ajout des règles de pare-feu à `ufw`.
   
   ```
   sudo ufw allow in on lxdbr0
   sudo ufw route allow in on lxdbr0
   sudo ufw route allow out on lxdbr0
   ```
    
3. Connexion au conteneur `lxc exec jupyterhub -- sudo --user ubuntu --login`
4. Test de la connexion internet `ping 8.8.8.8`

# À savoir
- Le fichier de config par défaut se retrouve dans `/etc/lxc/default.conf`

# Références
- [Installer JupyterHub](https://jupyterhub.readthedocs.io/en/stable/tutorial/quickstart.html)
- 