import streamlit as st
import pandas as pd
import pymysql
import altair as alt
def get_connection():
    return pymysql.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="2thB1wv7qzEZyNy.root",
        password="U9zVgW0YwRAhaKUi",
        database="RETAIL_ORDERS",
        port=4000,
        ssl={"ssl": {}},
    )
def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.set_page_config(page_title="RETAIL ORDER DATA ANALYSIS", page_icon="📊", layout="wide")
st.markdown('<p style="font-size:40px;font-weight:bold; color:red;"> RETAIL ORDER DATA ANALYSIS </p>', unsafe_allow_html=True)


#QUESTION-1-Find top 10 highest revenue generating products
st.sidebar.header("QUERY 1")
st.sidebar.subheader("Find top 10 highest revenue generating products")
show_query1=st.sidebar.button("Show revenue")
query="""select product_id,sub_category, sum(sale_price*quantity) as revenue
from RETAIL_ORDERS.DETAILS2
group by product_id,sub_category order by revenue desc limit 10"""
if show_query1:
  data_revenue=fetch_data(query)
  st.subheader("TOP 10 HIGHEST REVENUE GENERATING PRODUCTS")
  st.dataframe(data_revenue)
  chart = (
      alt.Chart(data_revenue)
      .mark_bar()
      .encode(
          x=alt.X("revenue:Q", title="TOTAL REVENUE"),
          y=alt.Y("product_id:N", title="PRODUCT ID",sort="-x"),
          color=alt.Color("revenue:Q", scale=alt.Scale(scheme="greens")),
          tooltip=["product_id","sub_category" ,"revenue"]
             )
             .properties(title="Top 10 Highest Revenue Generating Products", height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-2-Find the top 5 cities with the highest profit margins
st.sidebar.header("QUERY 2")
st.sidebar.subheader("Find the top 5 cities with the highest profit margins")
show_query2=st.sidebar.button("Show cities")
query="""select d.city, sum((ds.sale_price-ds.cost_price)/nullif(ds.sale_price, 0)) as profit_margin
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.city
order by profit_margin desc limit 5"""
if show_query2:
  data_cities=fetch_data(query)
  st.subheader("Top 5 CITIES WITH HIGHEST PROFIT MARGINS")
  st.dataframe(data_cities)
  chart = (
      alt.Chart(data_cities)
      .mark_bar()
      .encode(
          x=alt.X("profit_margin:Q", title="PROFIT MARGIN"),
          y=alt.Y("city:N", title="CITY", sort="-x"),
          color=alt.Color("profit_margin:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["profit_margin","city"]
             )
             .properties(title="Top 5 Cities with Highest Profit Margins", height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-3-Calculate the total discount given for each category
st.sidebar.header("QUERY 3")
st.sidebar.subheader("Calculate the total discount given for each category")
show_query3=st.sidebar.button("Show category")
query="""select d.category, sum(ds.discount*ds.quantity) as total_discount
from RETAIL_ORDERS.DETAILS1 d
left join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.category"""
if show_query3:
  data_discount=fetch_data(query)
  st.subheader("TOTAL DISCOUNT GIVEN FOR EACH CATEGORY")
  st.dataframe(data_discount)
  chart = (
      alt.Chart(data_discount)
      .mark_bar()
      .encode(
          x=alt.X("category:N", title="CATEGORY"),
          y=alt.Y("total_discount:Q", title="TOTAL DISCOUNT"),
          color=alt.Color("total_discount:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["total_discount","category"]
             )
             .properties(title="Total discount given for each category", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-4-Find the average sale price per product category
st.sidebar.header("QUERY 4")
st.sidebar.subheader("Find the average sale price per product category")
show_query4=st.sidebar.button("Show avg sale price")
query="""select d.category, sum(ds.sale_price*ds.quantity)/nullif(sum(ds.quantity),0) as average_sale_price
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.category"""
if show_query4:
  data_average_sale_price=fetch_data(query)
  st.subheader("AVERAGE SALE PRICE PER PRODUCT CATEGORY")
  st.dataframe(data_average_sale_price)
  chart = (
      alt.Chart(data_average_sale_price)
      .mark_bar()
      .encode(
          x=alt.X("category:N", title="CATEGORY"),
          y=alt.Y("average_sale_price:Q", title="AVERAGE SALE PRICE"),
          color=alt.Color("average_sale_price:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["average_sale_price","category"]
             )
             .properties(title="Average sale price per product category", height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-5-Find the region with the highest average sale price
st.sidebar.header("QUERY 5")
st.sidebar.subheader("Find the region with the highest average sale price")
show_query5=st.sidebar.button("Show region")
query="""select d.region, sum(ds.sale_price*ds.quantity)/nullif(sum(ds.quantity),0) as highest_avg_sale_price
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.region order by highest_avg_sale_price desc limit 1"""
if show_query5:
  data_region=fetch_data(query)
  st.subheader("REGION WITH THE HIGHEST AVERAGE SALE PRICE")
  st.dataframe(data_region)
  chart = (
      alt.Chart(data_region)
      .mark_bar()
      .encode(
          x=alt.X("region:N", title="CATEGORY"),
          y=alt.Y("highest_avg_sale_price:Q", title="TOTAL DISCOUNT"),
          color=alt.Color("highest_avg_sale_price:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["highest_avg_sale_price","region"]
             )
             .properties(title="Region with the highest average sale price", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-6-Find the total profit per category
st.sidebar.header("QUERY 6")
st.sidebar.subheader("Find the total profit per category")
show_query6=st.sidebar.button("Show total profit")
query="""select d.category, sum(ds.profit) as total_profit
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.category"""
if show_query6:
  data_total_profit=fetch_data(query)
  st.subheader("TOTAL PROFIT PER CATEGORY")
  st.dataframe(data_total_profit)
  chart = (
      alt.Chart(data_total_profit)
      .mark_bar()
      .encode(
          x=alt.X("category:N", title="CATEGORY"),
          y=alt.Y("total_profit:Q", title="TOTAL PROFIT"),
          color=alt.Color("total_profit:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["total_profit","category"]
             )
             .properties(title="Total profit per category", width=600, height=400)
          )
  st.altair_chart(chart, use_container_width=True)


#QUESTION-7-Identify the top 3 segments with the highest quantity of orders
st.sidebar.header("QUERY 7")
st.sidebar.subheader("Identify the top 3 segments with the highest quantity of orders")
show_query7=st.sidebar.button("Show segments")
query="""select d.segment, sum(ds.quantity) as total_quantity
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.segment order by total_quantity desc limit 3"""
if show_query7:
  data_segment=fetch_data(query)
  st.subheader("TOP 3 SEGMENTS WITH THE HIGHEST QUANTITY OF ORDERS")
  st.dataframe(data_segment)
  chart = (
      alt.Chart(data_segment)
      .mark_bar()
      .encode(
          x=alt.X("segment:N", title="SEGMENT"),
          y=alt.Y("total_quantity:Q", title="TOTAL QUANTITY"),
          color=alt.Color("total_quantity:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["total_quantity","segment"]
             )
             .properties(title="Top 3 segments with the highest quantity of orders",width=600, height=400)
          )
  st.altair_chart(chart, use_container_width=True)


#QUESTION-8-Determine the average discount percentage given per region
st.sidebar.header("QUERY 8")
st.sidebar.subheader("Determine the average discount percentage given per region")
show_query8=st.sidebar.button("Show avg d%")
query="""select d.region, sum(ds.discount_percent*ds.quantity)/nullif(sum(ds.quantity),0) as average_discount_percent
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.region"""
if show_query8:
  data_avg_discount_percent=fetch_data(query)
  st.subheader("AVERAGE DISCOUNT PERCENTAGE GIVEN PER REGION")
  st.dataframe(data_avg_discount_percent)
  chart = (
      alt.Chart(data_avg_discount_percent)
      .mark_bar()
      .encode(
          x=alt.X("region:N", title="REGION"),
          y=alt.Y("average_discount_percent:Q", title="AVERAGE DISCOUNT PERCENTAGE"),
          color=alt.Color("average_discount_percent:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["average_discount_percent","region"]
             )
             .properties(title="Average discount percentage given per region",width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-9-Find the product category with the highest total profit
st.sidebar.header("QUERY 9")
st.sidebar.subheader("Find the product category with the highest total profit")
show_query9=st.sidebar.button("Show product category")
query="""select d.category, sum(ds.profit) as total_profit
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.category order by total_profit desc limit 1"""
if show_query9:
  data_product_category=fetch_data(query)
  st.subheader("PRODUCT CATEGORY WITH THE HIGHEST TOTAL PROFIT")
  st.dataframe(data_product_category)
  chart = (
      alt.Chart(data_product_category)
      .mark_bar()
      .encode(
          x=alt.X("category:N", title="CATEGORY"),
          y=alt.Y("total_profit:Q", title="TOTAL PROFIT"),
          color=alt.Color("total_profit:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["total_profit","category"]
             )
             .properties(title="Region with the highest average sale price", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-10-Calculate the total revenue generated per year
st.sidebar.header("QUERY 10")
st.sidebar.subheader("Calculate the total revenue generated per year(Year-over-Year)")
show_query10=st.sidebar.button("Show revenue per year")
query="""select year(d.order_date) as year, sum(ds.sale_price*ds.quantity) as total_revenue
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by year order by total_revenue asc"""
if show_query10:
  data_yoy=fetch_data(query)
  st.subheader("TOTAL REVENUE GENERATED PER YEAR(Year-over-Year)")
  st.dataframe(data_yoy)
  chart = (
      alt.Chart(data_yoy)
      .mark_bar()
      .encode(
          x=alt.X("year:N", title="YEAR"),
          y=alt.Y("total_revenue:Q", title="TOTAL REVENUE"),
          color=alt.Color("total_revenue:Q", scale=alt.Scale(scheme="goldgreen")),
             )
             .properties(title="Total revenue generated per year(Year-over-Year)", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-11-Calculate the total revenue generated per month in 2023 (Monthly sales analysis-evaluate growth or decline in sales over different months)
st.sidebar.header("QUERY 11")
st.sidebar.subheader("Calculate the total revenue generated per month in 2023(Month-over-Month)")
show_query11=st.sidebar.button("Show revenue per month")
query="""select year(d.order_date) as year,
month(d.order_date) as month, sum(ds.sale_price * ds.quantity) as total_revenue
from RETAIL_ORDERS.DETAILS1 d
inner join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
where year(d.order_date)=2023
group by year,month
order by month asc"""
if show_query11:
  data_mom=fetch_data(query)
  st.subheader("TOTAL REVENUE GENERATED PER MONTH IN 2023(Month-over-Month)")
  st.dataframe(data_mom)
  chart = (
      alt.Chart(data_mom)
      .mark_bar()
      .encode(
          x=alt.X("month:N", title="MONTH",sort=alt.SortField("month", order="ascending")),
          y=alt.Y("total_revenue:Q", title="TOTAL REVENUE"),
          color=alt.Color("total_revenue:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["total_revenue","month","year"]
             )
             .properties(title="Total revenue generated per month in 2023(Month-over-Month)", width=600, height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-12-Identify top 10 products that are selling at loss due to high discounts.
st.sidebar.header("QUERY 12")
st.sidebar.subheader("Identify top 10 products that are selling at loss due to high discounts")
show_query12=st.sidebar.button("Show loss")
query="""select ds.product_id,ds.sub_category,d.category,sum(ds.discount_percent*ds.quantity)/nullif(sum(ds.quantity), 0) as average_discount_percent,
sum(ds.profit) as total_profit
from RETAIL_ORDERS.DETAILS2 ds
left join RETAIL_ORDERS.DETAILS1 d on ds.order_id=d.order_id
group by ds.product_id, ds.sub_category,d.category
having total_profit<0
order by total_profit asc limit 10"""
if show_query12:
  data_loss=fetch_data(query)
  st.subheader("TOP 10 PRODUCTS THAT ARE SELLING AT LOSS DUE TO HIGH DISCOUNTS")
  st.dataframe(data_loss)
  chart = (
      alt.Chart(data_loss)
      .mark_bar()
      .encode(
          x=alt.X("product_id:N", title="PRODUCT ID"),
          y=alt.Y("total_profit:Q", title="TOTAL PROFIT"),
          color=alt.Color("total_profit:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["product_id","total_profit","average_discount_percent"]
             )
             .properties(title="Top 10 products that are selling at loss due to high discounts", width=600, height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-13-Identify the most valuable segments based on order frequency and revenue.
st.sidebar.header("QUERY 13")
st.sidebar.subheader("Identify the most valuable segments based on order frequency and revenue")
show_query13=st.sidebar.button("Show valuable segment")
query="""select d.segment,count(d.order_id) as total_orders, sum(ds.sale_price*ds.quantity) as total_revenue,
avg(ds.sale_price*ds.quantity) as average_revenue_per_order
from RETAIL_ORDERS.DETAILS1 d
left join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.segment order by total_revenue desc"""
if show_query13:
  data_valuable_segment=fetch_data(query)
  st.subheader("MOST VALUABLE SEGMENTS BASED ON ORDER FREQUENCY AND REVENUE")
  st.dataframe(data_valuable_segment)
  chart = (
      alt.Chart(data_valuable_segment)
      .mark_bar()
      .encode(
          x=alt.X("segment:N", title="SEGMENT"),
          y=alt.Y("total_revenue:Q", title="TOTAL REVENUE"),
          color=alt.Color("total_revenue:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["total_revenue","average_revenue_per_order","segment","total_orders"]
             )
             .properties(title="Most valuable segments based on order frequency and revenue", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)


#QUESTION-14-Identify the top 2 best-performing regions based on revenue.
st.sidebar.header("QUERY 14")
st.sidebar.subheader("Identify the top 2 best-performing regions based on revenue")
show_query14=st.sidebar.button("Show best performing regions")
query="""select d.region, sum(ds.sale_price*ds.quantity) as total_revenue
from RETAIL_ORDERS.DETAILS1 d
left join RETAIL_ORDERS.DETAILS2 ds on d.order_id=ds.order_id
group by d.region order by total_revenue desc limit 2"""
if show_query14:
  data_performing_region=fetch_data(query)
  st.subheader("TOP 2 BEST-PERFORMING REGIONS BASED ON REVENUE")
  st.dataframe(data_performing_region)
  chart = (
      alt.Chart(data_performing_region)
      .mark_bar()
      .encode(
          x=alt.X("region:N", title="REGION"),
          y=alt.Y("total_revenue:Q", title="TOTAL REVENUE"),
          color=alt.Color("total_revenue:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["region","total_revenue"]
             )
             .properties(title="Top 2 best-performing regions based on revenue", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-15-Analyze sales impact of the products with average discount percent.
st.sidebar.header("QUERY 15")
st.sidebar.subheader("Analyze sales impact of the products with average discount percent")
show_query15=st.sidebar.button("Show sales impact")
query="""select discount_category, count(*) as num_product
from( select product_id, sub_category,
sum(discount_percent*quantity)/nullif(sum(quantity), 0) as average_discount_percent,
case when sum(discount_percent*quantity)/nullif(sum(quantity), 0)>20 then 'high discount'
when sum(discount_percent*quantity)/nullif(sum(quantity), 0) between 10 and 20 then 'medium discount'
else 'low discount'
end as discount_category
from RETAIL_ORDERS.DETAILS2
group by product_id, sub_category) as categorized group by discount_category"""
if show_query15:
  data_sales_impact=fetch_data(query)
  st.subheader("SALES IMPACT OF THE PRODUCTS WITH AVERAGE DISCOUNT PERCENT")
  st.dataframe(data_sales_impact)
  chart = (
      alt.Chart(data_sales_impact)
      .mark_bar()
      .encode(
          x=alt.X("discount_category:N", title="DISCOUNT CATEGORY"),
          y=alt.Y("num_product:Q", title="NUMBER OF PRODUCTS"),
          color=alt.Color("num_product:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["discount_category","num_product"]
             )
             .properties(title="Sales impact on products with average discount percentage", height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-16-Identify profitability of ship mode in different regions (top 4).
st.sidebar.header("QUERY 16")
st.sidebar.subheader("Identify profitability of ship mode in different regions(top 4)")
show_query16=st.sidebar.button("Show ship mode")
query="""select d.region, d.ship_mode, sum(ds.profit) as total_profit
from RETAIL_ORDERS.DETAILS2 ds
right join RETAIL_ORDERS.DETAILS1 d on ds.order_id=d.order_id
group by d.region, d.ship_mode
order by total_profit desc limit 4"""
if show_query16:
  data_ship_mode=fetch_data(query)
  st.subheader("PROFITABILITY OF SHIP MODE IN DIFFERENT REGIONS (TOP 4)")
  st.dataframe(data_ship_mode)
  chart = (
      alt.Chart(data_ship_mode)
      .mark_bar()
      .encode(
        x=alt.X("region:N", title="Region"),
        y=alt.Y("total_profit:Q", title="Total Profit"),
        color=alt.Color("total_profit:Q", scale=alt.Scale(scheme="goldgreen")),
        tooltip=["region", "ship_mode", "total_profit"]
             )
      .properties(title="Profitability of ship mode in different regions(top 4)", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-17-Analysing the product performance based on profit margin
st.sidebar.header("QUERY 17")
st.sidebar.subheader("Analysing the product performance based on profit margin")
show_query17=st.sidebar.button("Show product performance")
query="""select product_id, sub_category,
sum(sale_price*quantity) as total_revenue,
sum(profit) as total_profit,
case when sum(sale_price*quantity)=0 then 0
else sum(profit)/sum(sale_price*quantity)
end as profit_margin
from RETAIL_ORDERS.DETAILS2
group by product_id, sub_category order by profit_margin desc"""
if show_query17:
  data_product_performance=fetch_data(query)
  st.subheader("PRODUCT PERFORMANCE BASED ON PROFIT MARGIN")
  st.dataframe(data_product_performance)
  chart = (
      alt.Chart(data_product_performance)
      .mark_bar()
      .encode(
          x=alt.X("product_id:N", title="PRODUCT ID"),
          y=alt.Y("profit_margin:Q", title="PROFIT MARGIN"),
          color=alt.Color("profit_margin:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["profit_margin","product_id","total_revenue"]
             )
             .properties(title="Product performance based on profit margin", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-18-Find the top most 3 usable shipping modes
st.sidebar.header("QUERY 18")
st.sidebar.subheader("Find the top most 3 usable shipping modes")
show_query18=st.sidebar.button("Show usable shipping modes")
query="""select count(d.order_id) as total_orders,d.ship_mode, sum(profit) as profit
from RETAIL_ORDERS.DETAILS2 ds
right join RETAIL_ORDERS.DETAILS1 d on ds.order_id=d.order_id
group by d.ship_mode order by profit desc limit 3"""
if show_query18:
  data_most_usable_shipping_mode=fetch_data(query)
  st.subheader("TOP MOST 3 USABLE SHIPPING MODES")
  st.dataframe(data_most_usable_shipping_mode)
  chart = (
      alt.Chart(data_most_usable_shipping_mode)
      .mark_bar()
      .encode(
          x=alt.X("ship_mode:N", title="SHIP MODES"),
          y=alt.Y("total_orders:Q", title="TOTAL ORDERS"),
          color=alt.Color("total_orders:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["profit","ship_mode","total_orders"]
             )
             .properties(title="Top most 3 usable shipping modes", width=600,height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-19-Find top 10 states with High Revenue but Low Profit Margin percentage
st.sidebar.header("QUERY 19")
st.sidebar.subheader("Find top 10 states with High Revenue but Low Profit Margin percentage")
show_query19=st.sidebar.button("Show states")
query="""SELECT d.state, format(sum(ds.sale_price * ds.quantity),2) as total_revenue,
format((SUM(ds.profit) / NULLIF(SUM(ds.sale_price * ds.quantity), 0)) * 100, 2) as profit_margin_pecent
from RETAIL_ORDERS.DETAILS1 d
left join RETAIL_ORDERS.DETAILS2 ds on d.order_id = ds.order_id
group by d.state
having format((SUM(ds.profit) / NULLIF(SUM(ds.sale_price * ds.quantity), 0)) * 100, 2)< 10
order by total_revenue desc limit 10"""
if show_query19:
  data_state=fetch_data(query)
  st.subheader("TOP 10 STATES WITH HIGH REVENUE BUT LOW PROFIT MARGIN PERCENTAGE")
  st.dataframe(data_state)
  chart = (
      alt.Chart(data_state)
      .mark_bar()
      .encode(
          x=alt.X("state:N", title="STATE"),
          y=alt.Y("profit_margin_pecent:Q", title="PROFIT MARGIN PERCENTAGE"),
          color=alt.Color("profit_margin_pecent:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["profit_margin_pecent","state"]
             )
             .properties(title="Top 10 states with High Revenue but Low Profit Margin percentage",width=600, height=400)
          )
  st.altair_chart(chart, use_container_width=True)

#QUESTION-20-Find top 5 postal codes with high orders
st.sidebar.header("QUERY 20")
st.sidebar.subheader("Find top 5 postal codes with high orders")
show_query20=st.sidebar.button("Show postal codes")
query="""Select d.postal_code,d.city,count(d.order_id) as total_orders,
format(sum(ds.sale_price * ds.quantity),2) as total_revenue from RETAIL_ORDERS.DETAILS2 ds
right join RETAIL_ORDERS.DETAILS1 d on ds.order_id=d.order_id
group by postal_code,city order by total_orders desc limit 5"""
if show_query20:
  data_postal_code=fetch_data(query)
  st.subheader("TOP 5 POSTAL CODES WITH HIGH ORDERS")
  st.dataframe(data_postal_code)
  chart = (
      alt.Chart(data_postal_code)
      .mark_bar()
      .encode(
          y=alt.Y("postal_code:N", title="POSTAL CODE", sort="-x"),
          x=alt.X("total_orders:Q", title="TOTAL ORDERS"),
          color=alt.Color("total_orders:Q", scale=alt.Scale(scheme="goldgreen")),
          tooltip=["postal_code", "city","total_orders","total_revenue"]
             )
             .properties(title="Top 5 postal codes with high orders",height=400)
          )
  st.altair_chart(chart, use_container_width=True)
