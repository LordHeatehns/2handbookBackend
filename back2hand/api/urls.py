
from django.urls import path

from .views import CategoriesArticle, CategoriesComic, CategoriesEducation, CategoriesKnowledge, CategoriesManga, CategoriesNovel, DetailList ,ImageProfileAPI ,DetailUser , CreateProduct, ProductSearch , Test2 ,DeleteProduct , DetailPostSingle, UpdateImageBlob, UpdateStatus ,TestImage
from rest_framework.routers import DefaultRouter

app_name = 'api.urls'

'''router = DefaultRouter()
#router.register('',DetailList,basename = 'detail-shell')
router.register('detail',DetailList, basename ='detail_list')
router.register('image',ImageProfileAPI, basename = 'image-profile'),
router.register('detailUser',DetailUser,basename = 'detail-user'),
router.register('create',CreateProduct,basename ='create-product')
router.register('test',TestImages,basename ='test-img')


urlpatterns = router.urls'''

urlpatterns = [
    path('detail/',DetailList.as_view() , name='detail_list'),
    path('details/<str:pk>/',DetailPostSingle.as_view(), name = 'detail-single'),
    path('image/',ImageProfileAPI.as_view(),name='image-prfile'),
    path('detailUser/',DetailUser.as_view(),  name = 'detail-user'),
    path('create/',CreateProduct.as_view(),name = 'Create-product'),
    path('test/',Test2.as_view(),name = 'test'),
    path('delete/',DeleteProduct.as_view(),name='delete-product'),
    path('search/',ProductSearch.as_view(), name = 'search-dartail'),
    path('updateStatus/',UpdateStatus.as_view(), name ='Update_Status'),
    path('update/image/',UpdateImageBlob.as_view(),name='update-image'),
    path('categories/manga/',CategoriesManga.as_view(),name='Manga'),
    path('categories/novel/',CategoriesNovel.as_view(),name='Novel'),
    path('categories/article/',CategoriesArticle.as_view(),name='Article'),
    path('categories/knowledge/',CategoriesKnowledge.as_view(),name='Knowledge'),
    path('categories/comic/',CategoriesComic.as_view(),name='Comic'),
    path('categories/education/',CategoriesEducation.as_view(),name='Education'),







]


'''urlpatterns = [
    path('', PostList.as_view(), name='listpost'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('search/', PostListDetailfilter.as_view(), name='searchpost'),
    # Post Admin URLs
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]'''