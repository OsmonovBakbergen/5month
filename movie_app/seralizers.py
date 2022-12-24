from rest_framework import serializers
from movie_app.models import *


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = "id name movies_count".split()

    def get_movies_count(self, director):
        return director.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MoviesReviewsSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = "title description duration director reviews rating".split()

    def get_rating(self, movie):
        lst = [review.stars for review in movie.reviews.all()]
        return sum(lst) / len(lst)
