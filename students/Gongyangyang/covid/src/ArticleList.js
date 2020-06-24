import React, {Component} from "react";
import {Table} from 'antd';
import './App.css';

const {Column } = Table;

const articleList = [
    {
        "date": "2020-01-13",
        "today": {
            "confirm": 0,
            "suspect": 0,
            "heal": 0,
            "dead": 0,
            "severe": null,
            "storeConfirm": 0,
            "input": 0
        },
        "total": {
            "confirm": 41,
            "suspect": 0,
            "heal": 0,
            "dead": 1,
            "severe": null,
            "input": 0,
            "storeConfirm": 0
        },
        "extData": null,
        "lastUpdateTime": null
    },
    {
        "date": "2020-01-14",
        "today": {
            "confirm": 0,
            "suspect": 0,
            "heal": 0,
            "dead": 0,
            "severe": null,
            "storeConfirm": 0,
            "input": 0
        },
        "total": {
            "confirm": 41,
            "suspect": 0,
            "heal": 0,
            "dead": 1,
            "severe": null,
            "input": 0,
            "storeConfirm": 0
        },
        "extData": null,
        "lastUpdateTime": null
    },
  ];


class ArticleList extends Component {
    constructor(props) {
        super (props);
        this.state = { 
            articleList: articleList,
         }
    }

    render() {
        // return <div>第一个组件</div>;
        return (
          <Table dataSource ={this.state.articleList} pagination={{pageSize:10} } >
          <Column title ='序号' dataIndex='No' render ={(text,recorder,index) => <span>{index +1}</span>}/>
          <Column title ='日期' dataIndex='date' />
          <Column title ='新增确诊' dataIndex="confirm"  render={(text, record) => (<a>{record.today.confirm}</a>)}  />
          <Column title ='新增治愈' dataIndex='newheal' render={(text, record) => (<a>{record.today.heal}</a>)} />
          <Column title ='新增死亡' dataIndex='newdead' render={(text, record) => (<a>{record.today.dead}</a>)} />
          <Column title ='累计确诊' dataIndex='operate' render={(text, record) => (<a>{record.total.confirm}</a>)} />
          <Column title ='累计治愈' dataIndex='heal' render={(text, record) => (<a>{record.total.heal}</a>)} />
          <Column title ='累计死亡' dataIndex='dead' render={(text, record) => (<a>{record.total.dead}</a>)} />
          </Table>  
      
          );
    }

    componentDidMount() {
      fetch('/ug/api/wuhan/app/data/list-total?t=318561784801')
        .then(response => response.json())
        .then(result => this.setState({articleList: result.data.chinaDayList}))
        .catch(e => e);
    }
}

export default ArticleList;
