from config import *

class Menu:
    """gestion du menu"""

    def __init__(self,application, *groupes):
        self.color = dict(
            normal=(0,200,0),
            hover=(0,200,200),
        )
        font = pygame.font.SysFont('Harrington',24)
        items = (
            ('JOUER',application.partie),
            ('Options', application.partie),
            ('Quitter', application.quitter)
        )
        x = LARGEUR_FENETRE/2
        y = HAUTEUR_FENETRE/2

        self._boutons = []
        for texte, cmd in items:
            mb = MenuBouton(texte,self.color['normal'],font,x,y,300,40,cmd)
            self._boutons.append(mb)
            y += 64
            for groupe in groupes:
                groupe.add(mb)

    def update(self,events):
        clicGauche, *_ = pygame.mouse.get_pressed()
        posPointeur = pygame.mouse.get_pos()
        for bouton in self._boutons:
            if bouton.rect.collidepoint(*posPointeur):
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                bouton.dessiner(self.color['hover'])

                if clicGauche:
                    bouton.executerCommande()
                break
            else:
                bouton.dessiner(self.color['normal'])
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def detruire(self):
        pygame.mouse.set_cursor(*pygame.cursors.arrow)


class MenuBouton(pygame.sprite.Sprite):
    """ Création d'un simple bouton rectangulaire """
    def __init__(self, texte, couleur, font, x, y, largeur, hauteur, commande):
        super().__init__()
        self._commande = commande
        self.image = pygame.Surface((largeur, hauteur))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.texte = font.render(texte, True, (0, 0, 0))
        self.rectTexte = self.texte.get_rect()
        self.rectTexte.center = (int(largeur / 2), int(hauteur / 2))
        self.dessiner(couleur)

    def dessiner(self, couleur):
        self.image.fill(couleur)
        self.image.blit(self.texte, self.rectTexte)

    def executerCommande(self):
        # Appel de la commande du bouton
        self._commande()