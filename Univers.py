import random

class Univers:
    def __init__(self, etoile=0, planete=0, trou_noir=0, galaxie=0, asteroide=0, hydrogen=0,
                 helium=0, lithium=0, beryllium=0, boron=0, carbon=0, nitrogen=0, oxygen=0, fluorine=0,
                 neon=0, sodium=0, magnesium=0, aluminum=0, silicon=0, phosphorus=0, sulfur=0,
                 chlorine=0, argon=0, potassium=0, calcium=0, scandium=0, titanium=0, vanadium=0,
                 chromium=0, manganese=0, iron=0, cobalt=0, nickel=0, copper=0, zinc=0, gallium=0,
                 germanium=0, arsenic=0, selenium=0, bromine=0, krypton=0, rubidium=0, strontium=0,
                 yttrium=0, zirconium=0, niobium=0, molybdenum=0, technetium=0, ruthenium=0, rhodium=0,
                 palladium=0, silver=0, cadmium=0, indium=0, tin=0, antimony=0, tellurium=0, iodine=0,
                 xenon=0, cesium=0, barium=0, lanthanum=0, cerium=0, praseodymium=0, neodymium=0,
                 promethium=0, samarium=0, europium=0, gadolinium=0, terbium=0, dysprosium=0, holmium=0,
                 erbium=0, thulium=0, ytterbium=0, lutetium=0, hafnium=0, tantalum=0, tungsten=0, rhenium=0,
                 osmium=0, iridium=0, platinum=0, gold=0, mercury=0, thallium=0, lead=0, bismuth=0, polonium=0,
                 astatine=0, radon=0, francium=0, radium=0, actinium=0, thorium=0, protactinium=0, uranium=0,
                 neptunium=0, plutonium=0, americium=0, curium=0, berkelium=0, californium=0, einsteinium=0,
                 fermium=0, mendelevium=0, nobelium=0, lawrencium=0, rutherfordium=0, dubnium=0, seaborgium=0,
                 bohrium=0, hassium=0, meitnerium=0, darmstadtium=0, roentgenium=0, copernicium=0, nihonium=0,
                 flerovium=0, moscovium=0, livermorium=0, tennessine=0, oganesson=0):
        self.etoile = etoile
        self.planete = planete
        self.trou_noir = trou_noir
        self.galaxie = galaxie
        self.asteroide = asteroide
        self.hydrogen = hydrogen
        self.helium = helium
        self.lithium = lithium
        self.beryllium = beryllium
        self.boron = boron
        self.carbon = carbon
        self.nitrogen = nitrogen
        self.oxygen = oxygen
        self.fluorine = fluorine
        self.neon = neon
        self.sodium = sodium
        self.magnesium = magnesium
        self.aluminum = aluminum
        self.silicon = silicon
        self.phosphorus = phosphorus
        self.sulfur = sulfur
        self.chlorine = chlorine
        self.argon = argon
        self.potassium = potassium
        self.calcium = calcium
        self.scandium = scandium
        self.titanium = titanium
        self.vanadium = vanadium
        self.chromium = chromium
        self.manganese = manganese
        self.iron = iron
        self.cobalt = cobalt
        self.nickel = nickel
        self.copper = copper
        self.zinc = zinc
        self.gallium = gallium
        self.germanium = germanium
        self.arsenic = arsenic
        self.selenium = selenium
        self.bromine = bromine
        self.krypton = krypton
        self.rubidium = rubidium
        self.strontium = strontium
        self.yttrium = yttrium
        self.zirconium = zirconium
        self.niobium = niobium
        self.molybdenum = molybdenum
        self.technetium = technetium
        self.ruthenium = ruthenium
        self.rhodium = rhodium
        self.palladium = palladium
        self.silver = silver
        self.cadmium = cadmium
        self.indium = indium
        self.tin = tin
        self.antimony = antimony
        self.tellurium = tellurium
        self.iodine = iodine
        self.xenon = xenon
        self.cesium = cesium
        self.barium = barium
        self.lanthanum = lanthanum
        self.cerium = cerium
        self.praseodymium = praseodymium
        self.neodymium = neodymium
        self.promethium = promethium
        self.samarium = samarium
        self.europium = europium
        self.gadolinium = gadolinium
        self.terbium = terbium
        self.dysprosium = dysprosium
        self.holmium = holmium
        self.erbium = erbium
        self.thulium = thulium
        self.ytterbium = ytterbium
        self.lutetium = lutetium
        self.hafnium = hafnium
        self.tantalum = tantalum
        self.tungsten = tungsten
        self.rhenium = rhenium
        self.osmium = osmium
        self.iridium = iridium
        self.platinum = platinum
        self.gold = gold
        self.mercury = mercury
        self.thallium = thallium
        self.lead = lead
        self.bismuth = bismuth
        self.polonium = polonium
        self.astatine = astatine
        self.radon = radon
        self.francium = francium
        self.radium = radium
        self.actinium = actinium
        self.thorium = thorium
        self.protactinium = protactinium
        self.uranium = uranium
        self.neptunium = neptunium
        self.plutonium = plutonium
        self.americium = americium
        self.curium = curium
        self.berkelium = berkelium
        self.californium = californium
        self.einsteinium = einsteinium
        self.fermium = fermium
        self.mendelevium = mendelevium
        self.nobelium = nobelium
        self.lawrencium = lawrencium
        self.rutherfordium = rutherfordium
        self.dubnium = dubnium
        self.seaborgium = seaborgium
        self.bohrium = bohrium
        self.hassium = hassium
        self.meitnerium = meitnerium
        self.darmstadtium = darmstadtium
        self.roentgenium = roentgenium
        self.copernicium = copernicium
        self.nihonium = nihonium
        self.flerovium = flerovium
        self.moscovium = moscovium
        self.livermorium = livermorium
        self.tennessine = tennessine
        self.oganesson = oganesson



    @staticmethod
    def _validate_positive(value):
        if value < 0:
            raise ValueError("Value must be >= 0")
        return value

    # @property and @setter for each element
    @property
    def etoile(self):
        return self._etoile

    @etoile.setter
    def etoile(self, value):
        self._etoile = self._validate_positive(value)

    @property
    def planete(self):
        return self._planete

    @planete.setter
    def planete(self, value):
        self._planete = self._validate_positive(value)

    @property
    def trou_noir(self):
        return self._trou_noir

    @trou_noir.setter
    def trou_noir(self, value):
        self._trou_noir = self._validate_positive(value)

    @property
    def galaxie(self):
        return self._galaxie

    @galaxie.setter
    def galaxie(self, value):
        self._galaxie = self._validate_positive(value)

    @property
    def asteroide(self):
        return self._asteroide

    @asteroide.setter
    def asteroide(self, value):
        self._asteroide = self._validate_positive(value)

    @property
    def hydrogen(self):
        return self._hydrogen

    @hydrogen.setter
    def hydrogen(self, value):
        self._hydrogen = self._validate_positive(value)

    @property
    def helium(self):
        return self._helium

    @helium.setter
    def helium(self, value):
        self._helium = self._validate_positive(value)

    @property
    def lithium(self):
        return self._lithium

    @lithium.setter
    def lithium(self, value):
        self._lithium = self._validate_positive(value)

    @property
    def beryllium(self):
        return self._beryllium

    @beryllium.setter
    def beryllium(self, value):
        self._beryllium = self._validate_positive(value)

    @property
    def boron(self):
        return self._boron

    @boron.setter
    def boron(self, value):
        self._boron = self._validate_positive(value)

    @property
    def carbon(self):
        return self._carbon

    @carbon.setter
    def carbon(self, value):
        self._carbon = self._validate_positive(value)

    @property
    def nitrogen(self):
        return self._nitrogen

    @nitrogen.setter
    def nitrogen(self, value):
        self._nitrogen = self._validate_positive(value)

    @property
    def oxygen(self):
        return self._oxygen

    @oxygen.setter
    def oxygen(self, value):
        self._oxygen = self._validate_positive(value)

    @property
    def fluorine(self):
        return self._fluorine

    @fluorine.setter
    def fluorine(self, value):
        self._fluorine = self._validate_positive(value)

    @property
    def neon(self):
        return self._neon

    @neon.setter
    def neon(self, value):
        self._neon = self._validate_positive(value)

    @property
    def sodium(self):
        return self._sodium

    @sodium.setter
    def sodium(self, value):
        self._sodium = self._validate_positive(value)

    @property
    def magnesium(self):
        return self._magnesium

    @magnesium.setter
    def magnesium(self, value):
        self._magnesium = self._validate_positive(value)

    @property
    def aluminum(self):
        return self._aluminum

    @aluminum.setter
    def aluminum(self, value):
        self._aluminum = self._validate_positive(value)

    @property
    def silicon(self):
        return self._silicon

    @silicon.setter
    def silicon(self, value):
        self._silicon = self._validate_positive(value)

    @property
    def phosphorus(self):
        return self._phosphorus

    @phosphorus.setter
    def phosphorus(self, value):
        self._phosphorus = self._validate_positive(value)

    @property
    def sulfur(self):
        return self._sulfur

    @sulfur.setter
    def sulfur(self, value):
        self._sulfur = self._validate_positive(value)

    @property
    def chlorine(self):
        return self._chlorine

    @chlorine.setter
    def chlorine(self, value):
        self._chlorine = self._validate_positive(value)

    @property
    def argon(self):
        return self._argon

    @argon.setter
    def argon(self, value):
        self._argon = self._validate_positive(value)

    @property
    def potassium(self):
        return self._potassium

    @potassium.setter
    def potassium(self, value):
        self._potassium = self._validate_positive(value)

    @property
    def calcium(self):
        return self._calcium

    @calcium.setter
    def calcium(self, value):
        self._calcium = self._validate_positive(value)

    @property
    def scandium(self):
        return self._scandium

    @scandium.setter
    def scandium(self, value):
        self._scandium = self._validate_positive(value)

    @property
    def titanium(self):
        return self._titanium

    @titanium.setter
    def titanium(self, value):
        self._titanium = self._validate_positive(value)

    @property
    def vanadium(self):
        return self._vanadium

    @vanadium.setter
    def vanadium(self, value):
        self._vanadium = self._validate_positive(value)

    @property
    def chromium(self):
        return self._chromium

    @chromium.setter
    def chromium(self, value):
        self._chromium = self._validate_positive(value)

    @property
    def manganese(self):
        return self._manganese

    @manganese.setter
    def manganese(self, value):
        self._manganese = self._validate_positive(value)

    @property
    def iron(self):
        return self._iron

    @iron.setter
    def iron(self, value):
        self._iron = self._validate_positive(value)

    @property
    def cobalt(self):
        return self._cobalt

    @cobalt.setter
    def cobalt(self, value):
        self._cobalt = self._validate_positive(value)

    @property
    def nickel(self):
        return self._nickel

    @nickel.setter
    def nickel(self, value):
        self._nickel = self._validate_positive(value)

    @property
    def copper(self):
        return self._copper

    @copper.setter
    def copper(self, value):
        self._copper = self._validate_positive(value)

    @property
    def zinc(self):
        return self._zinc

    @zinc.setter
    def zinc(self, value):
        self._zinc = self._validate_positive(value)

    @property
    def gallium(self):
        return self._gallium

    @gallium.setter
    def gallium(self, value):
        self._gallium = self._validate_positive(value)

    @property
    def germanium(self):
        return self._germanium

    @germanium.setter
    def germanium(self, value):
        self._germanium = self._validate_positive(value)

    @property
    def arsenic(self):
        return self._arsenic

    @arsenic.setter
    def arsenic(self, value):
        self._arsenic = self._validate_positive(value)

    @property
    def selenium(self):
        return self._selenium

    @selenium.setter
    def selenium(self, value):
        self._selenium = self._validate_positive(value)

    @property
    def bromine(self):
        return self._bromine

    @bromine.setter
    def bromine(self, value):
        self._bromine = self._validate_positive(value)

    @property
    def krypton(self):
        return self._krypton

    @krypton.setter
    def krypton(self, value):
        self._krypton = self._validate_positive(value)

    @property
    def rubidium(self):
        return self._rubidium

    @rubidium.setter
    def rubidium(self, value):
        self._rubidium = self._validate_positive(value)

    @property
    def strontium(self):
        return self._strontium

    @strontium.setter
    def strontium(self, value):
        self._strontium = self._validate_positive(value)

    @property
    def yttrium(self):
        return self._yttrium

    @yttrium.setter
    def yttrium(self, value):
        self._yttrium = self._validate_positive(value)

    @property
    def zirconium(self):
        return self._zirconium

    @zirconium.setter
    def zirconium(self, value):
        self._zirconium = self._validate_positive(value)

    @property
    def niobium(self):
        return self._niobium

    @niobium.setter
    def niobium(self, value):
        self._niobium = self._validate_positive(value)

    @property
    def molybdenum(self):
        return self._molybdenum

    @molybdenum.setter
    def molybdenum(self, value):
        self._molybdenum = self._validate_positive(value)

    @property
    def technetium(self):
        return self._technetium

    @technetium.setter
    def technetium(self, value):
        self._technetium = self._validate_positive(value)

    @property
    def ruthenium(self):
        return self._ruthenium

    @ruthenium.setter
    def ruthenium(self, value):
        self._ruthenium = self._validate_positive(value)

    @property
    def rhodium(self):
        return self._rhodium

    @rhodium.setter
    def rhodium(self, value):
        self._rhodium = self._validate_positive(value)

    @property
    def palladium(self):
        return self._palladium

    @palladium.setter
    def palladium(self, value):
        self._palladium = self._validate_positive(value)

    @property
    def silver(self):
        return self._silver

    @silver.setter
    def silver(self, value):
        self._silver = self._validate_positive(value)

    @property
    def cadmium(self):
        return self._cadmium

    @cadmium.setter
    def cadmium(self, value):
        self._cadmium = self._validate_positive(value)

    @property
    def indium(self):
        return self._indium

    @indium.setter
    def indium(self, value):
        self._indium = self._validate_positive(value)

    @property
    def tin(self):
        return self._tin

    @tin.setter
    def tin(self, value):
        self._tin = self._validate_positive(value)

    @property
    def antimony(self):
        return self._antimony

    @antimony.setter
    def antimony(self, value):
        self._antimony = self._validate_positive(value)

    @property
    def tellurium(self):
        return self._tellurium

    @tellurium.setter
    def tellurium(self, value):
        self._tellurium = self._validate_positive(value)

    @property
    def iodine(self):
        return self._iodine

    @iodine.setter
    def iodine(self, value):
        self._iodine = self._validate_positive(value)

    @property
    def xenon(self):
        return self._xenon

    @xenon.setter
    def xenon(self, value):
        self._xenon = self._validate_positive(value)

    @property
    def cesium(self):
        return self._cesium

    @cesium.setter
    def cesium(self, value):
        self._cesium = self._validate_positive(value)

    @property
    def barium(self):
        return self._barium

    @barium.setter
    def barium(self, value):
        self._barium = self._validate_positive(value)

    @property
    def lanthanum(self):
        return self._lanthanum

    @lanthanum.setter
    def lanthanum(self, value):
        self._lanthanum = self._validate_positive(value)

    @property
    def cerium(self):
        return self._cerium

    @cerium.setter
    def cerium(self, value):
        self._cerium = self._validate_positive(value)

    @property
    def praseodymium(self):
        return self._praseodymium

    @praseodymium.setter
    def praseodymium(self, value):
        self._praseodymium = self._validate_positive(value)

    @property
    def neodymium(self):
        return self._neodymium

    @neodymium.setter
    def neodymium(self, value):
        self._neodymium = self._validate_positive(value)

    @property
    def promethium(self):
        return self._promethium

    @promethium.setter
    def promethium(self, value):
        self._promethium = self._validate_positive(value)

    @property
    def samarium(self):
        return self._samarium

    @samarium.setter
    def samarium(self, value):
        self._samarium = self._validate_positive(value)

    @property
    def europium(self):
        return self._europium

    @europium.setter
    def europium(self, value):
        self._europium = self._validate_positive(value)

    @property
    def gadolinium(self):
        return self._gadolinium

    @gadolinium.setter
    def gadolinium(self, value):
        self._gadolinium = self._validate_positive(value)

    @property
    def terbium(self):
        return self._terbium

    @terbium.setter
    def terbium(self, value):
        self._terbium = self._validate_positive(value)

    @property
    def dysprosium(self):
        return self._dysprosium

    @dysprosium.setter
    def dysprosium(self, value):
        self._dysprosium = self._validate_positive(value)

    @property
    def holmium(self):
        return self._holmium

    @holmium.setter
    def holmium(self, value):
        self._holmium = self._validate_positive(value)

    @property
    def erbium(self):
        return self._erbium

    @erbium.setter
    def erbium(self, value):
        self._erbium = self._validate_positive(value)

    @property
    def thulium(self):
        return self._thulium

    @thulium.setter
    def thulium(self, value):
        self._thulium = self._validate_positive(value)

    @property
    def ytterbium(self):
        return self._ytterbium

    @ytterbium.setter
    def ytterbium(self, value):
        self._ytterbium = self._validate_positive(value)

    @property
    def lutetium(self):
        return self._lutetium

    @lutetium.setter
    def lutetium(self, value):
        self._lutetium = self._validate_positive(value)

    @property
    def hafnium(self):
        return self._hafnium

    @hafnium.setter
    def hafnium(self, value):
        self._hafnium = self._validate_positive(value)

    @property
    def tantalum(self):
        return self._tantalum

    @tantalum.setter
    def tantalum(self, value):
        self._tantalum = self._validate_positive(value)

    @property
    def tungsten(self):
        return self._tungsten

    @tungsten.setter
    def tungsten(self, value):
        self._tungsten = self._validate_positive(value)

    @property
    def rhenium(self):
        return self._rhenium

    @rhenium.setter
    def rhenium(self, value):
        self._rhenium = self._validate_positive(value)

    @property
    def osmium(self):
        return self._osmium

    @osmium.setter
    def osmium(self, value):
        self._osmium = self._validate_positive(value)

    @property
    def iridium(self):
        return self._iridium

    @iridium.setter
    def iridium(self, value):
        self._iridium = self._validate_positive(value)

    @property
    def platinum(self):
        return self._platinum

    @platinum.setter
    def platinum(self, value):
        self._platinum = self._validate_positive(value)

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = self._validate_positive(value)

    @property
    def mercury(self):
        return self._mercury

    @mercury.setter
    def mercury(self, value):
        self._mercury = self._validate_positive(value)

    @property
    def thallium(self):
        return self._thallium

    @thallium.setter
    def thallium(self, value):
        self._thallium = self._validate_positive(value)

    @property
    def lead(self):
        return self._lead

    @lead.setter
    def lead(self, value):
        self._lead = self._validate_positive(value)

    @property
    def bismuth(self):
        return self._bismuth

    @bismuth.setter
    def bismuth(self, value):
        self._bismuth = self._validate_positive(value)

    @property
    def polonium(self):
        return self._polonium

    @polonium.setter
    def polonium(self, value):
        self._polonium = self._validate_positive(value)

    @property
    def astatine(self):
        return self._astatine

    @astatine.setter
    def astatine(self, value):
        self._astatine = self._validate_positive(value)

    @property
    def radon(self):
        return self._radon

    @radon.setter
    def radon(self, value):
        self._radon = self._validate_positive(value)

    @property
    def francium(self):
        return self._francium

    @francium.setter
    def francium(self, value):
        self._francium = self._validate_positive(value)

    @property
    def radium(self):
        return self._radium

    @radium.setter
    def radium(self, value):
        self._radium = self._validate_positive(value)

    @property
    def actinium(self):
        return self._actinium

    @actinium.setter
    def actinium(self, value):
        self._actinium = self._validate_positive(value)

    @property
    def thorium(self):
        return self._thorium

    @thorium.setter
    def thorium(self, value):
        self._thorium = self._validate_positive(value)

    @property
    def protactinium(self):
        return self._protactinium

    @protactinium.setter
    def protactinium(self, value):
        self._protactinium = self._validate_positive(value)

    @property
    def uranium(self):
        return self._uranium

    @uranium.setter
    def uranium(self, value):
        self._uranium = self._validate_positive(value)

    @property
    def neptunium(self):
        return self._neptunium

    @neptunium.setter
    def neptunium(self, value):
        self._neptunium = self._validate_positive(value)

    @property
    def plutonium(self):
        return self._plutonium

    @plutonium.setter
    def plutonium(self, value):
        self._plutonium = self._validate_positive(value)

    @property
    def americium(self):
        return self._americium

    @americium.setter
    def americium(self, value):
        self._americium = self._validate_positive(value)

    @property
    def curium(self):
        return self._curium

    @curium.setter
    def curium(self, value):
        self._curium = self._validate_positive(value)

    @property
    def berkelium(self):
        return self._berkelium

    @berkelium.setter
    def berkelium(self, value):
        self._berkelium = self._validate_positive(value)

    @property
    def californium(self):
        return self._californium

    @californium.setter
    def californium(self, value):
        self._californium = self._validate_positive(value)

    @property
    def einsteinium(self):
        return self._einsteinium

    @einsteinium.setter
    def einsteinium(self, value):
        self._einsteinium = self._validate_positive(value)

    @property
    def fermium(self):
        return self._fermium

    @fermium.setter
    def fermium(self, value):
        self._fermium = self._validate_positive(value)

    @property
    def mendelevium(self):
        return self._mendelevium

    @mendelevium.setter
    def mendelevium(self, value):
        self._mendelevium = self._validate_positive(value)

    @property
    def nobelium(self):
        return self._nobelium

    @nobelium.setter
    def nobelium(self, value):
        self._nobelium = self._validate_positive(value)

    @property
    def lawrencium(self):
        return self._lawrencium

    @lawrencium.setter
    def lawrencium(self, value):
        self._lawrencium = self._validate_positive(value)

    @property
    def rutherfordium(self):
        return self._rutherfordium

    @rutherfordium.setter
    def rutherfordium(self, value):
        self._rutherfordium = self._validate_positive(value)

    @property
    def dubnium(self):
        return self._dubnium

    @dubnium.setter
    def dubnium(self, value):
        self._dubnium = self._validate_positive(value)

    @property
    def seaborgium(self):
        return self._seaborgium

    @seaborgium.setter
    def seaborgium(self, value):
        self._seaborgium = self._validate_positive(value)

    @property
    def bohrium(self):
        return self._bohrium

    @bohrium.setter
    def bohrium(self, value):
        self._bohrium = self._validate_positive(value)

    @property
    def hassium(self):
        return self._hassium

    @hassium.setter
    def hassium(self, value):
        self._hassium = self._validate_positive(value)

    @property
    def meitnerium(self):
        return self._meitnerium

    @meitnerium.setter
    def meitnerium(self, value):
        self._meitnerium = self._validate_positive(value)

    @property
    def darmstadtium(self):
        return self._darmstadtium

    @darmstadtium.setter
    def darmstadtium(self, value):
        self._darmstadtium = self._validate_positive(value)

    @property
    def roentgenium(self):
        return self._roentgenium

    @roentgenium.setter
    def roentgenium(self, value):
        self._roentgenium = self._validate_positive(value)

    @property
    def copernicium(self):
        return self._copernicium

    @copernicium.setter
    def copernicium(self, value):
        self._copernicium = self._validate_positive(value)

    @property
    def nihonium(self):
        return self._nihonium

    @nihonium.setter
    def nihonium(self, value):
        self._nihonium = self._validate_positive(value)

    @property
    def flerovium(self):
        return self._flerovium

    @flerovium.setter
    def flerovium(self, value):
        self._flerovium = self._validate_positive(value)

    @property
    def moscovium(self):
        return self._moscovium

    @moscovium.setter
    def moscovium(self, value):
        self._moscovium = self._validate_positive(value)

    @property
    def livermorium(self):
        return self._livermorium

    @livermorium.setter
    def livermorium(self, value):
        self._livermorium = self._validate_positive(value)

    @property
    def tennessine(self):
        return self._tennessine

    @tennessine.setter
    def tennessine(self, value):
        self._tennessine = self._validate_positive(value)

    @property
    def oganesson(self):
        return self._oganesson

    @oganesson.setter
    def oganesson(self, value):
        self._oganesson = self._validate_positive(value)

    elements = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
        "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium",
        "Calcium",
        "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
        "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium",
        "Zirconium",
        "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium",
        "Tin",
        "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium",
        "Neodymium",
        "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium",
        "Ytterbium",
        "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
        "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
        "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium",
        "Einsteinium",
        "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium",
        "Hassium",
        "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium",
        "Tennessine", "Oganesson"
    ]

    def creuser(self):
        pass
