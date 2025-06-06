import streamlit as st
import pandas as pd
import sqlite3
import altair as alt
import plotly.graph_objects as go


def dashboard_todos():
    st.subheader("📊 Dashboard - Todos os Dados")
    
    try:
        
        conn = sqlite3.connect("mangaio.db")
        df = pd.read_sql_query("SELECT * FROM respostas_usuario", conn)

        if df.empty:
            st.info("Nenhuma resposta encontrada.")
            return

        #categoria e acertos
        resumo = df.groupby('categoria').agg(
            total_respostas=('acertou', 'count'),
            taxa_acerto=('acertou', 'mean')
        ).reset_index()

        resumo['taxa_acerto'] = (resumo['taxa_acerto'] * 100).round(2)

        fig = go.Figure()
        
        #gráfico de dois eixos
        # Barras - Total de Respostas
        fig.add_trace(go.Bar(
            x=resumo['categoria'],
            y=resumo['total_respostas'],
            name='Total de Respostas',
            yaxis='y1',
            marker_color='steelblue'
        ))

        # Linha - Taxa de Acerto (%)
        fig.add_trace(go.Scatter(
            x=resumo['categoria'],
            y=resumo['taxa_acerto'],
            name='Taxa de Acerto (%)',
            yaxis='y2',
            mode='lines+markers',
            line=dict(color='green', width=3)
        ))

        # Layout com dois eixos
        fig.update_layout(
            title='Desempenho por Categoria',
            xaxis=dict(title='Categoria'),
            yaxis=dict(
                title='Total de Respostas',
                side='left',
                showgrid=False
            ),
            yaxis2=dict(
                title='Taxa de Acerto (%)',
                overlaying='y',
                side='right',
                showgrid=False
            ),
            legend=dict(x=0.01, y=0.99),
            bargap=0.2,
            width=800,
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)


        # Tabela para separar acertos e erros por pergunta
        resumo = df.groupby(['categoria', 'quiz_id', 'pergunta']).agg(
            total_respostas=('acertou', 'count'),
            acertos=('acertou', 'sum'),
        ).reset_index()
        resumo['erros'] = resumo['total_respostas'] - resumo['acertos']

        # Pergunta com mais acertos por categoria
        mais_acertos = (
            resumo.sort_values(['categoria', 'acertos'], ascending=[True, False])
            .groupby('categoria')
            .first()
            .reset_index()
            .rename(columns={
                'pergunta': 'Pergunta com Mais Acertos',
                'acertos': 'Qtd Acertos'
            })
        )

        # Pergunta com mais erros por categoria
        mais_erros = (
            resumo.sort_values(['categoria', 'erros'], ascending=[True, False])
            .groupby('categoria')
            .first()
            .reset_index()
            .rename(columns={
                'pergunta': 'Pergunta com Mais Erros',
                'erros': 'Qtd Erros'
            })[['categoria', 'Pergunta com Mais Erros', 'Qtd Erros']]
        )

        # Unir as duas tabelas
        tabela_final = pd.merge(mais_acertos, mais_erros, on='categoria')

      
        st.write("#### 🏆 Perguntas com Mais Acertos e Erros por Categoria")
        st.dataframe(tabela_final, use_container_width=True)

    except Exception as e:
        st.error(f"Erro ao acessar os dados: {e}")
    finally:
        conn.close()
    
  
        
def dashboard_usuario():
    st.subheader("👤 Dashboard - Usuário")
    
    try:
       
        conn = sqlite3.connect("mangaio.db")
        df = pd.read_sql_query("SELECT * FROM respostas_usuario", conn)

        if df.empty:
            st.info("Nenhuma resposta registrada.")
            return

       
        if 'usuario_id' not in df.columns:
            st.error("A coluna 'usuario_id' não foi encontrada.")
            return

        
        usuarios = sorted(df['usuario_id'].unique())
        usuario_selecionado = st.selectbox("Selecione o usuário:", usuarios)

        # Filtrar dados 
        df_usuario = df[df['usuario_id'] == usuario_selecionado]

        st.markdown(f"### 📋 Resumo do Usuário `{usuario_selecionado}`")
        
        st.dataframe(df_usuario)

        if df_usuario.empty:
            st.warning("Este usuário ainda não respondeu nenhuma pergunta.")
            return

        # Verificar colunas necessárias
        if 'categoria' in df_usuario.columns and 'acertou' in df_usuario.columns:
           
            acertos_categoria = (
                df_usuario.groupby('categoria')['acertou']
                .sum()
                .reset_index(name='total_acertos')
            )

            # Gráfico de acertos por categoria
            chart = alt.Chart(acertos_categoria).mark_bar().encode(
                x=alt.X('categoria:N', title='Categoria'),
                y=alt.Y('total_acertos:Q', title='Total de Acertos'),
                tooltip=['categoria', 'total_acertos']
            ).properties(
                title='Acertos por Categoria',
                width=600,
                height=300
            )

            st.altair_chart(chart, use_container_width=True)
        else:
            st.warning("Colunas 'categoria' e/ou 'acertou' não estão disponíveis nos dados.")

    except sqlite3.Error as e:
        st.error(f"Erro ao acessar o banco de dados: {e}")
    finally:
        conn.close()
    