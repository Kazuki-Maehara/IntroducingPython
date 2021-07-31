import configparser


cfg = configparser.ConfigParser()
ret = cfg.read('minimalSettings.cfg')
print(ret)

print(cfg)

print(cfg['french'])

print(cfg['french']['greeting'])

print(cfg['files']['bin'])
