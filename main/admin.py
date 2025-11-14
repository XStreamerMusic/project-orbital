from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genre)

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'label_name', 'status', 'date_of_birth')
    list_filter = ('status', 'label')
    search_fields = ('name', 'alias')
    
    def label_name(self, obj):
        return obj.label.name if obj.label else "—"
    label_name.short_description = 'Record Label'

# Inline to show tracks under an album
class TrackInline(admin.TabularInline):
    model = Track
    extra = 0
    show_change_link = True


# Inline to show artists under a label
class ArtistInline(admin.TabularInline):
    model = Artist
    extra = 0
    fields = ('alias', 'status')
    show_change_link = True

    readonly_fields = ('alias', 'status')


# Inline to show albums under an artist
class AlbumInline(admin.TabularInline):
    model = Album.main_artists.through
    extra = 0
    verbose_name = "Main Album"
    verbose_name_plural = "Main Albums"
    show_change_link = True


# Inline to show tracks under an artist
class TrackInlineFromArtist(admin.TabularInline):
    model = Track.main_artists.through
    extra = 0
    verbose_name = "Main Track"
    verbose_name_plural = "Main Tracks"
    show_change_link = True


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'total_tracks', 'popularity')
    search_fields = ('title', 'platform_id')
    list_filter = ('release_date', 'popularity')
    filter_horizontal = ('images', 'main_artists', 'featured_artists', 'labels')

    inlines = [TrackInline]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'release_date', 'popularity')
    search_fields = ('title', 'platform_id')
    list_filter = ('release_date', 'popularity')
    filter_horizontal = ('images', 'main_artists', 'featured_artists')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_id', 'type', 'width', 'height')
    search_fields = ('image_id',)


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    inlines = [ArtistInline]