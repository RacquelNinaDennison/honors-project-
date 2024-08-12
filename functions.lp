#script (lua)

function uniform(ranks, statements)
    local ranks_l = ranks.number
    local statements_l = statements.number
    return statements_l / ranks_l
end

function modulo(statements, ranks)
    local ranks_l = ranks.number
    local statements_l = statements.number
    return statements_l - (math.floor(statements_l / ranks_l) * ranks_l)
end

function calculate_max_d(statements, ranks)
    local S = statements.number
    local R = ranks.number
    local max_d = (2 * S) / (R * (R - 1))
    return math.floor(max_d) 
end

function linear(statements, ranks, d)
    local rank_n = ranks.number
    local statements_n = statements.number
    local d_n = d.number
    local x = (statements_n - (rank_n * (rank_n - 1) * d_n) / 2) / rank_n
    if x ~= math.floor(x) then
        x = math.floor(x)
    end
    if x < 0 then
        local max_d = calculate_max_d(statements, ranks)
        if max_d == 0 then
            error("Cannot have a positive x with the given S and R. Increase S or decrease R.")
        else
            d_n = max_d
            x = (statements_n - (rank_n * (rank_n - 1) * d_n) / 2) / rank_n
            if x ~= math.floor(x) then
                x = math.floor(x)
            end
        end
    end
    
    return x, d_n
end

function linear_growth(statements, ranks, position)
    local rank_n = ranks.number
    local statements_n = statements.number
    local position_n = position.number
    local start, d_n = linear(statements, ranks, { number = 2 })
    local index_value = start + d_n * position_n
    return index_value
end


function linear_decline(statements, ranks, position)
    local rank_n = ranks.number
    local statements_n = statements.number
    local position_n = position.number
    local start, d_n = linear(statements, ranks, { number = 2 })
    local index_value = start - d_n * position_n
    return index_value
end

function ensure_directory_exists(directory)
    local success, err = os.execute("mkdir -p " .. directory)
    if not success then
        error("Could not create directory: " .. err)
    end
end

function write_distribution_to_file(distribution, s, r)
    local path = "random_files/"
    ensure_directory_exists(path)
    local rank_n = r.number
    local statements_n = s.number
    local file_name = string.format("random_distribution_%d_%d.txt", statements_n, rank_n)
    local file_path = path .. file_name
    local file, err = io.open(file_path, "w")
    if not file then
        error("Could not open file for writing: " .. err)
    end
    for i = 1, #distribution do
        file:write(distribution[i] .. "\n")
    end
    file:close()
end

function init_distribution(statements, ranks)
    local rank_n = ranks.number
    local statements_n = statements.number
    local distribution = {}
    local sum = 0

    for i = 1, rank_n do
        distribution[i] = 1
        sum = sum + 1
    end

    local remaining_statements = statements_n - sum
    while remaining_statements > 0 do
        local index = math.random(1, rank_n)
        distribution[index] = distribution[index] + 1
        remaining_statements = remaining_statements - 1
    end

    write_distribution_to_file(distribution, statements, ranks)
    return distribution
end

function random_index(statements, ranks, position)
    local path = "random_files/"
    local rank_n = ranks.number
    local statements_n = statements.number
    local file_name = string.format("random_distribution_%d_%d.txt", statements_n, rank_n)
    local file_path = path .. file_name
    local file, err = io.open(file_path, "r")
    if not file then
        print("File does not exist, initializing distribution...")
        init_distribution(statements, ranks)
        file, err = io.open(file_path, "r")
        if not file then
            error("Could not open file for reading after initialization: " .. err)
        end
    end
    
    local dist = {}
    local i = 1
    for line in file:lines() do
        dist[i] = tonumber(line)
        i = i + 1
    end
    file:close()

    return dist[position.number + 1]
end

#end.



