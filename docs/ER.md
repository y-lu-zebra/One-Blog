# ER 図

```mermaid
erDiagram
    auth_user           ||--o{ api_series : "user_created_id,user_updated_id"
    auth_user           ||--o{ api_categories : "user_created_id,user_updated_id"
    auth_user           ||--o{ api_posts : "user_created_id,user_updated_id"
    api_categories      |o--o{ api_posts : "category_id"
    api_posts           ||--o{ api_post_tag_rel : "post_id"
    api_post_tag_rel    }o--|| api_tags : "tag_id"
    api_posts           ||--o{ api_post_series_rel : "post_id"
    api_post_series_rel }o--|| api_series : "series_id"
    api_series          |o--o{ api_series : "parent_id"
    api_categories      |o--o{ api_categories : "parent_id"
    auth_user           ||--o{ api_tags : "user_created_id,user_updated_id"

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
        bigint parent_id
        integer user_created_id
        integer user_updated_id
        integer hits_count
        boolean is_published
    }

    api_categories {
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
        varchar(3) type
        bigint parent_id
        integer user_created_id
        integer user_updated_id
        integer hits_count
        boolean is_published
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
        bigint category_id
        integer user_created_id
        integer user_updated_id
        integer hits_count
        boolean is_published
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
        integer hits_count
        boolean is_published
    }

    api_post_series_rel {
        bigint id
        bigint post_id
        bigint series_id
    }

    api_post_tag_rel {
        bigint id
        bigint post_id
        bigint tag_id
    }
```
