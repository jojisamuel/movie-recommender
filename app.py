import streamlit as st
import pickle

def recommend(movie):
    movie_index =movies_list[movies_list['title']==movie].index[0]
    distances =similarity[movie_index]
    movies_list1 =sorted(list(enumerate(distances)) ,reverse=True ,key=lambda x :x[1])[1:6]
    L=[]
    for i in movies_list1:
        L.append(movies_list.iloc[i[0]].title)
    return L

st.title('Movie Recommender System')
movies_list=pickle.load(open('moviesdb2.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies_title=movies_list['title'].values
sel_option=st.selectbox('Movie',movies_title )

if st.button('Recommend'):
    recon=recommend(sel_option)
    for i in recon:
        st.write(i)