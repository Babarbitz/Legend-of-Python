import pytest

from config.window import *
from actor.aquamentus import *
from actor.boss import *
from actor.constants import *
from actor.enemy import *
from actor.fireball import *
from actor.item import *
from actor.keese import *
from actor.stalfos import *

# Unit Test template
#
#class TestName:
#
#    def setup_method(self, method):
#        
#
#    def test_namebutkeepthetestingront(self):
#        assert statement

class TestAquamentus:

    def setup_method(self,method):
        self.a = Aquamentus(0,0)
    
    def test_setup(self):
        assert(self.a.rect.x == 0)
        assert(self.a.rect.y == 0 + Y_OFFSET)

    def test_swapDirection(self):
        assert(self.a.xSpeed == AQUAMENTUS_SPEED)
        self.a.swapDirection()
        assert(self.a.xSpeed == -1 * AQUAMENTUS_SPEED)
    
    def test_attack(self):
        assert(self.a.isAttacking == False)
        self.a.attack()
        assert(self.a.isAttacking == True)

class TestBoss:

    def setup_method(self,method):
        self.b = Boss(0,0)
    
    def test_setup(self):
        assert(self.b.rect.x == 0)
        assert(self.b.rect.y == 0 + Y_OFFSET)

    def test_move(self):
        self.b.xSpeed = 3
        self.b.move()
        assert(self.b.rect.x == 3)
        assert(self.b.rect.y == 0 + Y_OFFSET)

    def test_hit(self):
        self.b.hit(1)
        assert(self.b.isHit == True)

class TestEnemy:

    def setup_method(self,method):
        self.e = Enemy(0,0)
    
    def test_setup(self):
        assert(self.e.rect.x == 0)
        assert(self.e.rect.y == 0 + Y_OFFSET)

    def test_move(self):
        self.e.xSpeed = 3
        self.e.move()
        assert(self.e.rect.x == 3)
        assert(self.e.rect.y == 0 + Y_OFFSET)

    def test_hit(self):
        self.e.hit(1)
        assert(self.e.isHit == True)

class TestFireball:

    def setup_method(self,method):
        self.f = Fireball(0,0,0,0)
    
    def test_setup(self):
        assert(self.f.rect.x == 0)
        assert(self.f.rect.y == 0)
        assert(self.f.xSpeed == 0)
        assert(self.f.ySpeed == 0)

    def test_start(self):
        self.f.start(10,10,2,2)
        assert(self.f.rect.x == 10)
        assert(self.f.rect.y == 10)
        assert(self.f.xSpeed == 2)
        assert(self.f.ySpeed == 2)

    def test_end(self):
        self.f.end()
        assert(self.f.rect.x == -1000)
        assert(self.f.rect.y == -1000)
        assert(self.f.xSpeed == 0)
        assert(self.f.ySpeed == 0)

    def test_move(self):
        self.f.start(10,10,2,2)
        self.f.move()
        assert(self.f.rect.x == 12)
        assert(self.f.rect.y == 12)
        assert(self.f.xSpeed == 2)
        assert(self.f.ySpeed == 2)

class TestItem:

    def setup_method(self,method):
        self.i = Item(0,0,2)
    
    def test_setup(self):
        assert(self.i.rect.x == 0)
        assert(self.i.rect.y == 0)
        assert(self.i.type == 2)

class TestKeese:


    def setup_method(self,method):
        self.k = Keese(0,0)

    def test_setup(self):
        assert(self.k.rect.x == 0)
        assert(self.k.rect.y == 0 + Y_OFFSET)

    def test_genRestLength(self):
        self.k.genRestLength()
        assert(self.k.restTime == 1 or self.k.restTime == 2)
        assert(self.k.restStartFrame == self.k.frameCounter)

    def test_genTravelPoint(self):
        self.k.genTravelPoint()
        magnitude = (abs(self.k.travelPoint[0] - self.k.rect.x)**2 + abs(self.k.travelPoint[1] - self.k.rect.y)**2)**(1/2)
        assert(magnitude >= KEESE_MAGNITUDE_MIN)
    
    def test_switchSprite(self):
        assert(self.k.spriteIndex == 0)
        self.k.switchSprite()
        assert(self.k.spriteIndex == 1)
    
    def test_stop(self):
        self.k.stop()
        assert(self.k.xSpeed == 0)
        assert(self.k.ySpeed == 0)
    
    def test_setMoveSpeed(self):
        self.k.travelPoint = [0,20]
        self.k.setMoveSpeed()
        assert(abs(self.k.xSpeed) == KEESE_MIN_SPEED)
        assert(abs(self.k.ySpeed) == KEESE_MAX_SPEED)

class TestStalfos:

    def setup_method(self,method):
        self.s = Stalfos(0,0)
    
    def test_setup(self):
        assert(self.s.rect.x == 0)
        assert(self.s.rect.y == 0 + Y_OFFSET)

    def test_genTravelPath(self):
        self.s.genTravelPath()
        assert(0 <= self.s.direction and self.s.direction <= 3)
        assert(0 <= self.s.walkFrames and self.s.walkFrames <= 3*60)

    def test_setWalkSpeed(self):
        self.s.direction = 2
        self.s.setWalkSpeed()
        assert(self.s.ySpeed == STALFOS_SPEED)
        self.s.direction = 1
        self.s.setWalkSpeed()
        assert(self.s.xSpeed == STALFOS_SPEED)

    def test_stop(self):
        self.s.stop()
        assert(self.s.xSpeed == 0)
        assert(self.s.ySpeed == 0)