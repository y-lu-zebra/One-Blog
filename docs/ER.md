# ER 図

```mermaid
erDiagram
    auth_user       ||--o{ api_series : "user_created_id,user_updated_id"
    auth_user       ||--o{ api_categories : "user_created_id,user_updated_id"
    auth_user       ||--o{ api_posts : "user_created_id,user_updated_id"
    auth_user       ||--o{ api_tags : "user_created_id,user_updated_id"
    auth_user       ||--o{ api_post_tag_rel : "user_created_id"
    api_series      |o--o{ api_posts : "series_id"
    api_categories  |o--o{ api_posts : "category_id"
    api_posts       ||--o{ api_post_tag_rel : "post_id"
    api_tags        ||--o{ api_post_tag_rel : "tag_id"
    api_series      |o--o{ api_series : "parent_id"
    api_categories  |o--o{ api_categories : "parent_id"

    auth_user {
        integer id
        varchar(128) password
        timestamp last_login
        boolean is_superuser
        varchar(150) username
        varchar(150) first_name
        varchar(150) last_name
        varchar(254) email
        boolean is_staff
        boolean is_active
        timestamp date_joined
    }

    api_series {
        bigint id
        timestamp date_created
        varchar(100) alias
        varchar(255) url
        integer sort_order
        varchar(255) meta_title
        text meta_description
        text meta_keywords
        timestamp date_updated
        varchar(100) name
        integer user_created_id
        bigint parent_id
        integer user_updated_id
    }

    api_categories {
        bigint id
        timestamp date_created
        varchar(255) url
        integer sort_order
        timestamp date_updated
        varchar(100) name
        varchar(100) alias
        integer user_created_id
        integer user_updated_id
        text meta_description
        text meta_keywords
        varchar(255) meta_title
        bigint parent_id
    }

    api_posts {
        bigint id
        timestamp date_created
        varchar(100) alias
        varchar(255) url
        integer sort_order
        varchar(255) meta_title
        text meta_description
        text meta_keywords
        timestamp date_updated
        varchar(255) title
        text overview
        text content
        integer user_created_id
        integer user_updated_id
        bigint category_id
    }

    api_tags {
        bigint id
        timestamp date_created
        varchar(100) alias
        varchar(255) url
        integer sort_order
        varchar(255) meta_title
        text meta_description
        text meta_keywords
        timestamp date_updated
        varchar(100) name
        integer user_created_id
        integer user_updated_id
    }

    api_post_tag_rel {
        bigint id
        timestamp date_created
        integer user_created_id
        bigint post_id
        bigint tag_id
    }
```
