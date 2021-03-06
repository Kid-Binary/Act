import React, { Component } from "react";
import { Link } from "react-router";
import { translate } from "react-i18next";

import generateUrl from "Router/generateUrl";

@translate(["buttons"])
class Categories extends Component{

    constructor(props){
        super(props);
        
    }
    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.categories.length > 0){
            return true;
        }
        return false;
    }
    renderCategory(categories, query, url){
        return categories.map((category) => {

            let activeClass = (query.project_area == category.id) ? "active" : "",
                params = {
                    centres: query.centres,
                    project_area: category.id
                };

            return(
                <li key={ category.id } class={ activeClass }>
                    <Link to={{ pathname: url, query: params }}>{ category.title }</Link>
                </li>
            );
        });
    }
    render(){
        let categories = this.props.categories,
            location = this.props.location,
            query = location.query,
            url = generateUrl("projects"),
            activeClass = !query.project_area ? "active" : "";

        return(
            <div class="categories-holder">
                <ul>
                    <li class={ activeClass }>
                        <Link to={{ pathname: url, query: {centres: query.centres} }}>{ this.props.t("buttons:all") }</Link>
                    </li>
                    { this.renderCategory(categories, query, url) }
                </ul>
            </div>
        );
    }

}

export default Categories;