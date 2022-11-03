# -F22-Cloud-Project_MS3-Contacts

## Associated Database Tables
1. columbia_students: [cuid, first_name, middle_name, last_name, email,school_code]
2. emails: [cuid, email, kind]
3. phones: [cuid, phone, kind]
4. addresses: [cuid, address, kind]

## Routes
- **students/\<uni>/phones**: returns the [cuid, email, kind] of student with associated with \<uni>
- **students/\<uni>/emails**: [cuid, phone, kind] of student with associated with \<uni>
- **students/\<uni>/addresses**: [cuid, address, kind] of student with associated with \<uni>

