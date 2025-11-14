from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Image(models.Model):
    ART_TYPES = [
        ('cover', 'Cover'),
        ('thumbnail', 'Thumbnail')
    ]

    title = models.CharField(max_length=50, blank=True)
    image_id = models.CharField(max_length=100, default="0")
    type = models.CharField(max_length=50, choices=ART_TYPES, blank=True)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)

    @property
    def direct_url(self):
        return f"https://drive.google.com/uc?export=view&id={self.image_id}"

    def __str__(self):
        return f"{self.image_id} ({self.width}x{self.height})"
    

class Label(models.Model):
    name = models.CharField(max_length=255)
    platform_id = models.CharField(max_length=255, unique=True)  # Unique platform-specific ID
    founded = models.DateField(null=True, blank=True)  # Optional: When the label was founded
    country = CountryField(blank=True)  # Optional: Label's country of origin
    logo = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)  # Optional: logo image from Image model
    
    # instagram = models.URLField(blank=True, null=True)
    # facebook = models.URLField(blank=True, null=True)
    # twitter = models.URLField(blank=True, null=True)

    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Artist(models.Model):

    STATUSES = [
        ('global', 'Global'),
        ('continental', 'Continental'),
        ('multi-national', 'Multi-National'),
        ('national', 'National'),
        ('hype', 'Hype'),
        ('upcoming', 'Upcoming'),
        ('underground', 'Underground'),
        ('monitoring', 'Monitoring'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUSES, default='national')
    images = models.ManyToManyField(Image, related_name="images", blank=True)

    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True, blank=True, related_name='signed_artists')
    genres = models.ManyToManyField(Genre, related_name="genres", blank=True)
    
    # # Optional social links
    # instagram = models.URLField(blank=True, null=True)
    # facebook = models.URLField(blank=True, null=True)
    # twitter = models.URLField(blank=True, null=True)

    # # DSPs
    # spotify = models.URLField(blank=True, null=True)
    # apple_music = models.URLField(blank=True, null=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alias or self.name
    

class Album(models.Model):
    
    title = models.CharField(max_length=255)

    # Foreign Keys
    main_artists = models.ManyToManyField(Artist, related_name="main_albums")
    featured_artists = models.ManyToManyField(Artist, related_name="featured_albums", blank=True)
    labels = models.ManyToManyField(Label, related_name="albums", blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name="albums")

    images = models.ManyToManyField(Image, related_name='albums')
    total_tracks = models.PositiveIntegerField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField()

    popularity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def __str__(self):
        return self.title
    
    @property
    def featured_artist_names(self):
        return ", ".join(a.name for a in self.featured_artists.all())


class Track(models.Model):
    
    title = models.CharField(max_length=255)

    # Foreign Keys
    main_artists = models.ManyToManyField(Artist, related_name="main_tracks")
    featured_artists = models.ManyToManyField(Artist, related_name="featured_tracks", blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")
    labels = models.ManyToManyField(Label, related_name="tracks", blank=True)
    genres = models.ManyToManyField(Genre, blank=True, related_name="tracks")
    

    images = models.ManyToManyField(Image, related_name='tracks')
    duration = models.PositiveIntegerField()
    release_date = models.DateField()
    popularity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    def __str__(self):
        return self.title
    
    @property
    def featured_artist_names(self):
        return ", ".join(a.name for a in self.featured_artists.all())