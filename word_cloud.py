from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text, max_words=2000, width=800, height=300, background_color="black", colormap="magma"):
    """
    Generates a word cloud from the given text.

    Args:
        text (str): The text to generate the word cloud from.
        max_words (int, optional): The maximum number of words to include in the word cloud. Defaults to 200.
        width (int, optional): The width of the generated image in pixels. Defaults to 800.
        height (int, optional): The height of the generated image in pixels. Defaults to 400.
        background_color (str, optional): The background color of the generated image. Defaults to "white".
        colormap (str, optional): The colormap to use for the words. Defaults to "viridis".  Other options include 'plasma', 'inferno', 'magma', 'cividis'.
    Returns:
        matplotlib.pyplot.Figure: The generated word cloud image.  Use plt.show() to display it.
    """

    wordcloud = WordCloud(
        width=width,
        height=height,
        max_words=max_words,
        background_color=background_color,
        colormap=colormap,
        #stopwords=STOPWORDS
    ).generate(text)


    plt.figure(figsize=(width/100, height/100), dpi=100)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    return plt

if __name__ == '__main__':

    text = """
    Apache Spark Apache Hive Kafka Airflow Hadoop HDFS Automic Scala DataFrame Datasets rdd Databricks
    ADF Glue EMR S3 EC2 Athena Redshift Apache Flink Spark Streaming Delta Delta tables Lambda
    Unity_Catalog CDF Auto_loader Parquet ORC JSON CSV Pandas Job_scheduler Threads parallel_processing Docker Data_quality ETL
    Sqoop Python PySpark SQL Postgres SCD Dimensions Facts GitHub Git CI/CD Kafka Airflow ADF AWS Azure Databricks
    ETL EMR Modeling Streaming CDC SQL DSA Python PySpark Vacuum API JIRA KPI timebox Data_Quality Normalization Schema Evolution
    SCD Merge Database Branching CDC Data_Warehouse Data_mart Datalake Lakehouse Medallion
    Partition Bucketing Optimization Joins Modeling Petabyte AWS ADLS RDBMS On_Prem Visualisation
    Medallion Yaml semi_structured Cloud XML Python Scala Azure JVM Parquet Docker Redshift Dimensions SCD
    """
    # Generate and display the word cloud
    wordcloud_figure = generate_word_cloud(text)
    wordcloud_figure.show() # added show here in main

    #plt.savefig('my_word_cloud.png')
    #plt.savefig('my_word_cloud.svg')
    print("Word cloud generated and displayed!")
