""" Models to manage the Waste Collection points
"""
from logging import getLogger
from django_orion_model.models import OrionEntity, OrionCharField, OrionTextField, OrionFloatField, OrionDateTimeField,\
    OrionIntegerField, OrionURLField, FamilyOrionEntity, OrionJSONField, OrionDecimalField


logger = getLogger(__name__)


class Agent(FamilyOrionEntity):
    FAMILY = "Agent"

    class Meta:
        abstract = True


class AgentType(FamilyOrionEntity):
    FAMILY = "AgentType"

    class Meta:
        abstract = True


class DepositPointType(Agent):

    class Meta:
        """ This made available to declare model in models package instead of models.py"""
        app_label = 'w4t_waste_collection'

    """Model of the collection point that determine common properties of some collection point"""
    name = OrionCharField(max_length=1024)
    # Set to to Reference
    # refInputs = OrionCharField()
    # Set to to Reference
    # refOutputs = OrionCharField()
    width = OrionFloatField(blank=True)
    height = OrionFloatField(blank=True)
    deep = OrionFloatField(blank=True)
    weight = OrionFloatField(blank=True)
    cargoVolume = OrionFloatField(blank=True)
    maximumLoad = OrionFloatField(blank=True)
    recommendedLoad = OrionFloatField(blank=True)
    category = OrionCharField(max_length=1024, choices=(
        ("trashCan", "trashCan"), ("bulk", "bulk"), ("wheelieBin", "wheelieBin"), ("bag", "bag"),
        ("fixed collection centers", "fixed collection centers"),
        ("mobile collection centers", "mobile collection centers"), ("underground", "underground"),
        ("pneumatic", "pneumatic"), ("portable", "portable")))
    insertHoleNumber = OrionIntegerField(blank=True)
    insertHoleWidth = OrionFloatField(blank=True)
    insertHoleHeight = OrionFloatField(blank=True)
    loadType = OrionCharField(blank=True, max_length=1024,
                              choices=(('side', 'side'), ('upper', 'upper'), ('front', 'front')))
    madeOf = OrionCharField(blank=True, max_length=1024)
    madeOfCodes = OrionCharField(blank=True, max_length=1024)
    brandName = OrionCharField(blank=True, max_length=1024)
    modelName = OrionCharField(blank=True, max_length=1024)
    manufacturerName = OrionCharField(blank=True, max_length=1024)
    # Set to JSON
    colors = OrionCharField(blank=True, max_length=1024)
    image = OrionURLField(blank=True)
    # set to Json
    compliantWith = OrionCharField(blank=True, max_length=1024)
    accessLimitation = OrionCharField(blank=True, max_length=1024)
    userIdentification = OrionCharField(blank=True, max_length=1024,
                                        choices=(("nfc", "nfc"), ("rfid", "rfid"), ("qr code", "qr code")))
    inputControl = OrionCharField(blank=True, max_length=1024,
                                  choices=(("chamber", "chamber"), ("weight", "weight"), ("volume", "volume")))
    maximumInputVolume = OrionFloatField(blank=True)
    # maximumInputVolume_meta = OrionCharField(blank=True)
    # Set to json
    features = OrionCharField(blank=True, max_length=1024)


class DepositPointIsle(Agent):
    """ A group of DepositPoints that belong together in a geographic area. This can be useful for calculations at
    DepositPointIsle level where there are more than one DepositPoint in a place and users tend to use them
    indifferently resulting in irregular measurements"""

    location = OrionCharField(max_length=1024)
    address = OrionTextField(blank=True, max_length=1024)
    name = OrionCharField(max_length=1024)
    description = OrionTextField(blank=True)
    features = OrionTextField(blank=True)
    # TODO TALK THIS TO ANDER
#     @property
#     def refCollectionPoints(self):
#         return self.collectionpoint_set.all()
#

    areaServed = OrionCharField(blank=True, max_length=1024)
    dateModified = OrionDateTimeField(blank=True)
    dateCreated = OrionDateTimeField(blank=True)


class DepositPoint(Agent):
    """Place where waste is deposited for its collection. It cover from traditional containers to less usual methods
    such as a personal plastic bag (in door2door systems), pneumatic waste dumpsters, fixed collection centers,mobile
    collection centers, etc."""

    ORION_TYPE = "DepositPoint"
    serialNumber = OrionCharField(max_length=1024)
    refSortingType = OrionCharField(max_length=1024)

    description = OrionTextField(blank=True)
    refType = OrionCharField(max_length=1024)
    storedWasteOrigin = OrionCharField(blank=True, max_length=1024)
    location = OrionJSONField()
    address = OrionTextField(blank=True)
    fillingLevel = OrionDecimalField(max_digits=2, decimal_places=1, blank=True)
    cargoWeight = OrionFloatField(blank=True)
    temperature = OrionFloatField(blank=True)
    methaneConcentration = OrionFloatField(blank=True)
    regulations = OrionCharField(blank=True, max_length=1024)
    responsible = OrionCharField(max_length=1024)
    owner = OrionCharField(max_length=1024)

    dateServiceStarted = OrionDateTimeField(blank=True)
    dateLastEmptying = OrionDateTimeField(blank=True)
    nextActuationDeadline = OrionDateTimeField(blank=True)

    # http://schema.org/openingHours
    actuationHours = OrionCharField(blank=True, max_length=1024)
    openingHours = OrionCharField(blank=True, max_length=1024)

    dateLastCleaning = OrionDateTimeField(blank=True)
    nextCleaningDeadline = OrionDateTimeField(blank=True)

    status = OrionCharField(blank=True, max_length=1024)
    color = OrionCharField(blank=True, max_length=1024)
    image = OrionURLField(blank=True)
    annotations = OrionTextField(blank=True)
    areaServed = OrionCharField(blank=True, max_length=1024)
    dateModified = OrionDateTimeField(blank=True)
    refDevice = OrionCharField(blank=True, max_length=1024)
