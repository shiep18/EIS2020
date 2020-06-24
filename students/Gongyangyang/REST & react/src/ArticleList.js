import React, {Component} from "react";

const articleList = [
    {
      "id": 2,
      "title": "React",
      "body": "React is good",
      "created": "2020-03-21T21:19:31.732703",
      "updated": "2020-03-21T21:19:31.732728"
    },
    {
      "id": 1,
      "title": "React",
      "body": "React is good",
      "created": "2020-03-21T21:10:53.922033",
      "updated": "2020-03-21T21:10:53.922128"
    }
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
            <div className="ArticleList">
                {this.state.articleList.map(item =>
          <div key={item.id}>
            <h4>{item.title}</h4>
            <p>
              <strong>{item.content}</strong>
              <br/>
              <em>创建时间：{item.pub_date}</em>
              <br/>
              <em>更新时间：{item.updated}</em>
            </p>
          </div>
        )}
      </div>
          );
    }

    componentDidMount() {
        fetch('/articles/')
          .then(response => response.json())
          .then(result => this.setState({articleList: result}))
          .catch(e => e);
      }
}

export default ArticleList;